import json
import urllib.request
import urllib.parse
import time
import webbrowser
import os
import sys

# Official GitHub CLI client_id for device flow
CLIENT_ID = "178c6fc778334803505d"

def start_device_flow():
    url = "https://github.com/login/device/code"
    data = urllib.parse.urlencode({
        "client_id": CLIENT_ID,
        "scope": "repo,workflow,read:user"
    }).encode("utf-8")
    
    req = urllib.request.Request(url, data=data, headers={
        "Accept": "application/json",
        "User-Agent": "Antigravity-F1-Dashboard"
    })
    
    try:
        with urllib.request.urlopen(req) as resp:
            res = json.loads(resp.read().decode("utf-8"))
            return res
    except Exception as e:
        print(f"Error starting device flow: {e}")
        return None

def poll_for_token(device_code, interval=5, expires_in=900):
    url = "https://github.com/login/oauth/access_token"
    start_time = time.time()
    
    while time.time() - start_time < expires_in:
        time.sleep(interval)
        data = urllib.parse.urlencode({
            "client_id": CLIENT_ID,
            "device_code": device_code,
            "grant_type": "urn:ietf:params:oauth:grant-type:device_code"
        }).encode("utf-8")
        
        req = urllib.request.Request(url, data=data, headers={
            "Accept": "application/json",
            "User-Agent": "Antigravity-F1-Dashboard"
        })
        
        try:
            with urllib.request.urlopen(req) as resp:
                res = json.loads(resp.read().decode("utf-8"))
                if "access_token" in res:
                    return res["access_token"]
                elif res.get("error") == "authorization_pending":
                    print(".", end="", flush=True)
                    continue
                elif res.get("error") == "slow_down":
                    time.sleep(5)
                else:
                    print(f"\nOAuth error: {res.get('error_description', res.get('error'))}")
                    return None
        except Exception as e:
            print(f"\nRequest error: {e}")
            time.sleep(interval)
            
    print("\nDevice flow timed out.")
    return None

if __name__ == "__main__":
    flow = start_device_flow()
    if not flow:
        sys.exit(1)
        
    user_code = flow["user_code"]
    verify_url = flow["verification_uri"]
    device_code = flow["device_code"]
    interval = flow.get("interval", 5)
    
    print("\n" + "="*60)
    print("GITHUB ONE-CLICK LOGIN")
    print("="*60)
    print(f"1. Open URL: {verify_url}")
    print(f"2. Enter Code: {user_code}")
    print("="*60 + "\n")
    
    # Save code to a status file so agent or user can see it
    status_file = r"C:\Users\Main User\.gemini\antigravity\scratch\f1-race-strategy-dashboard\github_auth_status.json"
    with open(status_file, "w", encoding="utf-8") as f:
        json.dump({
            "user_code": user_code,
            "verification_uri": verify_url,
            "device_code": device_code,
            "status": "pending"
        }, f)
        
    # Open browser automatically for user
    try:
        webbrowser.open(verify_url)
    except:
        pass
        
    print(f"Waiting for authorization (Code: {user_code})...", end="", flush=True)
    token = poll_for_token(device_code, interval)
    
    if token:
        print("\n[+] Authorization successful!")
        # Save token securely in project directory
        with open(r"C:\Users\Main User\.gemini\antigravity\scratch\f1-race-strategy-dashboard\.gh_token", "w", encoding="utf-8") as f:
            f.write(token)
            
        with open(status_file, "w", encoding="utf-8") as f:
            json.dump({"status": "authorized"}, f)
            
        # Now automatically deploy
        import github_deployer
        res = github_deployer.deploy_to_github(token, "f1-race-strategy-dashboard")
        if res:
            print("\n" + "="*60)
            print(f"SUCCESS! Repository: {res['repo_url']}")
            print(f"LIVE LAUNCH LINK:   {res['pages_url']}")
            print("="*60)
            with open(status_file, "w", encoding="utf-8") as f:
                json.dump({
                    "status": "deployed",
                    "repo_url": res["repo_url"],
                    "pages_url": res["pages_url"]
                }, f)
    else:
        print("\n[-] Authorization failed or timed out.")
