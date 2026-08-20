from jsonpath import jsonpath
import requests

def test_login():
    resp=requests.post(url='http://43.133.227.52/api/login',
                       json={'username':'tester',
                             'password':'123456'})
    assert resp.status_code==200
    assert int(resp.json()['code'])==0
if __name__=='__main__':
    resp=requests.post(url='http://43.133.227.52/api/login',
                       json={'username':'tester',
                             'password':'123456'}).json()
    token=jsonpath(resp,'$.token')
    print(token)