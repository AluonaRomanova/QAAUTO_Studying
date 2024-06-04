import requests

class GitHub:

    '''def get_user_defunkt(self):
        r=requests.get('https://api.github.com/users/defunkt')
        body=r.json()
        return body
    
    def get_non_exist_user(self):
        r=requests.get('https://api.github.com/users/butenkosergii')
        body=r.json()
        return body'''
    
    def get_user(self,username):
        r=requests.get(f'https://api.github.com/users/{username}')
        body=r.json()
        return body
    def search_repo(self,name):
        r=requests.get("https://api.github.com/search/repositories",params={"q":name})
        body=r.json()
        return body
    
    def get_jj(self):
        r=requests.get('https://api.github.com/emojis')
        #print(r.status_code)
        #body=r.json()
        return r
    
    def search_commits(self,owner,repo):
        r=requests.get(f"https://api.github.com/repos/{owner}/{repo}/commits")
        body=r.json()
        print(f"Response Status Code is {r.status_code}") 
        return body    
