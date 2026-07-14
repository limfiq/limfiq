
import json
import urllib.request

def main():
    url = "https://api.github.com/users/limfiq/repos?sort=updated&per_page=100"
    with urllib.request.urlopen(url) as f:
        repos = json.load(f)
    
    deployed_repos = []
    for repo in repos:
        if repo.get("homepage") or repo.get("has_pages"):
            deployed_repos.append({
                "name": repo["name"],
                "description": repo["description"],
                "language": repo["language"],
                "html_url": repo["html_url"],
                "homepage": repo["homepage"],
                "has_pages": repo["has_pages"]
            })
    
    print("Deployed repos:")
    print(json.dumps(deployed_repos, indent=2))

if __name__ == "__main__":
    main()
