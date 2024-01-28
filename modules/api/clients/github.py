import requests


class GitHub:

    def get_user(self, username):
        r = requests.get(f"https://api.github.com/users/{username}")
        body = r.json()
        
        return body
    

    def search_repo(self, name):
        r = requests.get("https://api.github.com/search/repositories", params={"q": name})
        body = r.json()
        
        return body

    def get_emojis(self):
        r = requests.get(f"https://api.github.com/emojis")
        body = r.json()
        
        return body

    def get_commits(self, owner_name, repo_name):
        r = requests.get(f"https://api.github.com/repos/{owner_name}/{repo_name}/commits")
        body = r.json()
        
        return body

    def get_code_frequency(self, owner_name, repo_name):
        r = requests.get(f"https://api.github.com/repos/{owner_name}/{repo_name}/stats/code_frequency")
        body = r.json()
        
        return body

    def get_branches(self, owner_name, repo_name):
        r = requests.get(f"https://api.github.com/repos/{owner_name}/{repo_name}/branches")
        body = r.json()
        
        return body
    