## made by x3bdulaziz
## wordprss REST API enumeration tool

#
import requests
import sys
import os
import concurrent.futures
#
#1. Check input 
if len(sys.argv) < 2:
    print("Usage: python3 wp_enum.py <target_url>")
    print("Example: python3 wp_enum.py http://example.com")
    print("Please add the full URL like https://example.com or http://example.com")
    sys.exit(1)

user_input = sys.argv[1].strip()
target_url = user_input.split("/wp-json")[0].rstrip("/") # Remove trailing slash if exists

#2. check URL 
if not target_url.startswith(("http://", "https://")):
    target_url = "http://" + target_url

#3. core Scanning function wp rest api
def enum_scan(user,user_id):
    
    scan_url = f"{user}/wp-json/wp/v2/users/{user_id}"
    try: 
        response = requests.get(scan_url,timeout=3)
        if response.status_code == 200:
            user_data = response.json()

            username=user_data.get("slug")
            disply_name = user_data.get("name")
            print(f"Found user| ID: {user_id:<10} | username: {username} | name {disply_name}")
    
    except requests.exceptions.RequestException:
        pass

#4.multi-threaded execution.
def run():
    print(f"strating wordpress enumeration on target:  {target_url}")
    print("-------------------------------------------------------------------+")
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
         for user_id in range(1,11):
            executor.submit(enum_scan,target_url,user_id)



if __name__ =="__main__":
    try:
        run()
    except KeyboardInterrupt:
        os._exit(0)


#end 
#date: 6/11/2026