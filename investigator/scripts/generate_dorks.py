import sys

def generate_dorks(name, location=None, username=None):
    name_q = f'"{name}"'
    dorks = []
    
    # 1. Social Media
    sites = [
        "linkedin.com", "facebook.com", "twitter.com", "instagram.com", 
        "tiktok.com", "reddit.com", "youtube.com", "pinterest.com"
    ]
    for site in sites:
        dorks.append(f'site:{site} {name_q}')
    
    # 2. Files
    filetypes = ["pdf", "doc", "docx", "xls", "xlsx", "ppt", "pptx"]
    for ft in filetypes:
        dorks.append(f'filetype:{ft} {name_q}')
    
    # 3. Legal / Concerning
    keywords = [
        "arrest", "court", "criminal", "jail", "prison", "warrant", 
        "lawsuit", "verdict", "scam", "fraud", "allegations", 
        "misconduct", "banned", "suspended", "fired", "investigation"
    ]
    for kw in keywords:
        dorks.append(f'{name_q} {kw}')
    
    # 4. Location specific if provided
    if location:
        dorks.append(f'{name_q} "{location}"')
        dorks.append(f'{name_q} "{location}" police')
        dorks.append(f'{name_q} "{location}" court')
    
    # 5. Username specific if provided
    if username:
        dorks.append(f'"{username}"')
        # Check specific sites for username
        for site in sites:
            dorks.append(f'site:{site} "{username}"')

    # Print dorks
    print("\n--- Generated Google Dorks ---")
    for d in dorks:
        print(d)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python generate_dorks.py \"<Target Name>\" [Location] [Username]")
        sys.exit(1)
    
    target_name = sys.argv[1]
    target_location = sys.argv[2] if len(sys.argv) > 2 else None
    target_username = sys.argv[3] if len(sys.argv) > 3 else None
    
    generate_dorks(target_name, target_location, target_username)
