import pytest
from modules.api.clients.github import GitHub

@pytest.mark.api
def test_user_exists(github_api):
   # api=GitHub()  - ПЕРЕНОС В ФИКСТУРУ
   # user=api.get_user(username='defunkt')
    user=github_api.get_user(username='defunkt')
    assert user['login']=='defunkt'

@pytest.mark.api
def test_user_not_exists(github_api):
   # api=GitHub()   - перенос в фикстуру conftest.py
   # r=api.get_user(username='butenkosergii')
    r=github_api.get_user(username='butenkosergii')
   # print(r)

    assert r['message']=='Not Found'

@pytest.mark.api
def test_repo_can_be_found(github_api):
    r=github_api.search_repo(name='become-qa-auto')
    #print(r)
    assert r['total_count']==57
    assert 'become-qa-auto' in r['items'][0]['name']

@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    r=github_api.search_repo(name='sergiibutenko_repo_non_exist')
   # print(r)
    assert r['total_count']==0

@pytest.mark.api
def test_repo_with_single_char_be_found(github_api):
    r=github_api.search_repo(name='s')
   # print(r)
    assert r['total_count']!=0


@pytest.mark.api
def test_jj(github_api):
    r=github_api.get_jj()
    q=r.json()
    #print(f"Response Body is {r.text}")         
    print(f"Response Status Code is {r.status_code}") 
    assert r.status_code == 200
    assert 'beetle' in q

@pytest.mark.api
def test_commit_can_be_found(github_api):
    r=github_api.search_commits(owner='AluonaRomanova',repo='QAAUTO_Studying')
    print(r[0])
    assert r[0]['sha']=='8598873e2b9d08095794cabbaee97984e854a968'
    assert r[0]['commit']['author']['name'] =='Alyona Romanova'
    assert r[0]['commit']['author']['email'] =='bastasi@gmail.com'
    assert r[0]['commit']['message']=='Mod16 done Pytest_ Project#3'
    
