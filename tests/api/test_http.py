import pytest
import requests

@pytest.mark.http
def test_first_request():
    r=requests.get('https://api.github.com/zen')
    print(f"Response is {r.text}")

@pytest.mark.http
def test_second_request():
    r = requests.get('https://api.github.com/users/defunkt')
   # print(f"Response Body is {r.text}")    1
    #print(f"Response Body is {r.json()}")             2
    #print(f"Response Status Code is {r.status_code}") 2
    #print(f"Response Headers are {r.headers}")        2

    body=r.json()
    assert body['name'] == 'Chris Wanstrath'

    assert r.status_code == 200

    headers=r.headers
    assert headers['Server'] == 'GitHub.com'

@pytest.mark.http
def test_status_code_request():
    r=requests.get('https://api.github.com/users/sergii_butenko')
    r.status_code==404
    print(f"Response Status Code is {r.status_code}")