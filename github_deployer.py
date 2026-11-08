import os
import json
import base64
import urllib.request
import urllib.error

PROJECT_DIR = r"C:\Users\Main User\.gemini\antigravity\scratch\f1-race-strategy-dashboard"

def deploy_to_github(token, repo_name="f1-race-strategy-dashboard", is_private=False):
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json",
        "User-Agent": "Antigravity-F1-Platform"
    }

    # 1. Get authenticated user
    req = urllib.request.Request("https://api.github.com/user", headers=headers)
    try:
        with urllib.request.urlopen(req) as resp:
            user_data = json.loads(resp.read().decode("utf-8"))
            username = user_data["login"]
            print(f"[+] Authenticated as GitHub user: {username}")
    except urllib.error.HTTPError as e:
        print(f"[-] Authentication failed: HTTP {e.code} - {e.read().decode('utf-8')}")
        return None

    # 2. Check if repo exists, if not create it
    repo_url = f"https://api.github.com/repos/{username}/{repo_name}"
    req_check = urllib.request.Request(repo_url, headers=headers)
    repo_exists = False
    try:
        with urllib.request.urlopen(req_check) as resp:
            repo_exists = True
            print(f"[+] Repository '{repo_name}' already exists.")
    except urllib.error.HTTPError as e:
        if e.code == 404:
            repo_exists = False
        else:
            print(f"[-] Error checking repo: {e}")
            return None

    if not repo_exists:
        print(f"[+] Creating repository '{repo_name}' on GitHub...")
        create_payload = json.dumps({
            "name": repo_name,
            "description": "Formula 1 Race Telemetry & Strategy Analytics Platform | Project #32",
            "private": is_private,
            "auto_init": True
        }).encode("utf-8")
        req_create = urllib.request.Request("https://api.github.com/user/repos", data=create_payload, headers=headers, method="POST")
        try:
            with urllib.request.urlopen(req_create) as resp:
                print(f"[+] Repository '{repo_name}' created successfully!")
        except urllib.error.HTTPError as e:
            print(f"[-] Failed to create repo: HTTP {e.code} - {e.read().decode('utf-8')}")
            return None

    # 3. Collect files to upload
    files_to_upload = []
    # Relevant files to publish
    include_exts = {".html", ".md", ".json", ".csv", ".xlsx", ".jpg", ".png", ".py"}
    exclude_dirs = {".git", ".tools", "__pycache__", ".cache"}

    for root, dirs, files in os.walk(PROJECT_DIR):
        dirs[:] = [d for d in dirs if d not in exclude_dirs]
        for f in files:
            ext = os.path.splitext(f)[1].lower()
            if ext in include_exts:
                full_p = os.path.join(root, f)
                rel_p = os.path.relpath(full_p, PROJECT_DIR).replace("\\", "/")
                # Don't upload b64 text cache
                if "b64" in f.lower() or "temp" in f.lower():
                    continue
                files_to_upload.append((rel_p, full_p))

    print(f"[+] Found {len(files_to_upload)} files to push to GitHub.")

    # 4. Upload blobs using GitHub Git Data API
    tree_items = []
    for rel_path, full_path in files_to_upload:
        with open(full_path, "rb") as fp:
            content_bytes = fp.read()
        
        # Check if text or binary
        is_binary = any(rel_path.endswith(ext) for ext in [".jpg", ".png", ".xlsx", ".zip"])
        if is_binary:
            encoding = "base64"
            content_str = base64.b64encode(content_bytes).decode("utf-8")
        else:
            encoding = "utf-8"
            try:
                content_str = content_bytes.decode("utf-8")
            except UnicodeDecodeError:
                encoding = "base64"
                content_str = base64.b64encode(content_bytes).decode("utf-8")

        blob_payload = json.dumps({
            "content": content_str,
            "encoding": encoding
        }).encode("utf-8")

        req_blob = urllib.request.Request(f"https://api.github.com/repos/{username}/{repo_name}/git/blobs", data=blob_payload, headers=headers, method="POST")
        try:
            with urllib.request.urlopen(req_blob) as resp:
                blob_data = json.loads(resp.read().decode("utf-8"))
                tree_items.append({
                    "path": rel_path,
                    "mode": "100644",
                    "type": "blob",
                    "sha": blob_data["sha"]
                })
                print(f"    Uploaded: {rel_path}")
        except urllib.error.HTTPError as e:
            print(f"[-] Failed to upload {rel_path}: {e}")

    # 5. Create Tree
    tree_payload = json.dumps({"tree": tree_items}).encode("utf-8")
    req_tree = urllib.request.Request(f"https://api.github.com/repos/{username}/{repo_name}/git/trees", data=tree_payload, headers=headers, method="POST")
    with urllib.request.urlopen(req_tree) as resp:
        tree_data = json.loads(resp.read().decode("utf-8"))
        tree_sha = tree_data["sha"]
        print(f"[+] Created Git tree: {tree_sha[:8]}")

    # 6. Get Parent Commit (latest on main/master)
    parent_sha = None
    branch = "main"
    for test_branch in ["main", "master"]:
        ref_url = f"https://api.github.com/repos/{username}/{repo_name}/git/ref/heads/{test_branch}"
        try:
            with urllib.request.urlopen(urllib.request.Request(ref_url, headers=headers)) as resp:
                ref_data = json.loads(resp.read().decode("utf-8"))
                parent_sha = ref_data["object"]["sha"]
                branch = test_branch
                break
        except urllib.error.HTTPError:
            pass

    # 7. Create Commit
    commit_body = {
        "message": "Formula 1 Race Strategy & Telemetry Analytics Platform (Project #32)",
        "tree": tree_sha
    }
    if parent_sha:
        commit_body["parents"] = [parent_sha]

    req_commit = urllib.request.Request(
        f"https://api.github.com/repos/{username}/{repo_name}/git/commits",
        data=json.dumps(commit_body).encode("utf-8"),
        headers=headers,
        method="POST"
    )
    with urllib.request.urlopen(req_commit) as resp:
        commit_data = json.loads(resp.read().decode("utf-8"))
        new_commit_sha = commit_data["sha"]
        print(f"[+] Created commit: {new_commit_sha[:8]}")

    # 8. Update Reference (push to branch)
    update_ref_url = f"https://api.github.com/repos/{username}/{repo_name}/git/refs/heads/{branch}"
    req_update = urllib.request.Request(
        update_ref_url,
        data=json.dumps({"sha": new_commit_sha, "force": True}).encode("utf-8"),
        headers=headers,
        method="PATCH"
    )
    try:
        with urllib.request.urlopen(req_update) as resp:
            print(f"[+] Updated branch '{branch}' successfully!")
    except urllib.error.HTTPError:
        # If ref doesn't exist yet, create it
        create_ref_url = f"https://api.github.com/repos/{username}/{repo_name}/git/refs"
        req_new_ref = urllib.request.Request(
            create_ref_url,
            data=json.dumps({"ref": f"refs/heads/{branch}", "sha": new_commit_sha}).encode("utf-8"),
            headers=headers,
            method="POST"
        )
        with urllib.request.urlopen(req_new_ref) as resp:
            print(f"[+] Created branch '{branch}' with new commit!")

    # 9. Enable GitHub Pages
    pages_url = f"https://api.github.com/repos/{username}/{repo_name}/pages"
    req_pages = urllib.request.Request(
        pages_url,
        data=json.dumps({"source": {"branch": branch, "path": "/"}}).encode("utf-8"),
        headers=headers,
        method="POST"
    )
    pages_live_url = f"https://{username.lower()}.github.io/{repo_name}/"
    try:
        with urllib.request.urlopen(req_pages) as resp:
            print(f"[+] GitHub Pages enabled!")
    except urllib.error.HTTPError as e:
        # Might already be enabled or building
        print(f"[*] GitHub Pages note: {e.code}")

    repo_html_url = f"https://github.com/{username}/{repo_name}"
    return {
        "username": username,
        "repo_name": repo_name,
        "repo_url": repo_html_url,
        "pages_url": pages_live_url
    }

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        tok = sys.argv[1]
        rname = sys.argv[2] if len(sys.argv) > 2 else "f1-race-strategy-dashboard"
        res = deploy_to_github(tok, rname)
        if res:
            print("\n" + "="*50)
            print(f"SUCCESS! Repository: {res['repo_url']}")
            print(f"LIVE LAUNCH LINK (GitHub Pages): {res['pages_url']}")
            print("="*50)
    else:
        print("Usage: python github_deployer.py <GITHUB_TOKEN> [REPO_NAME]")
