from jsonpath import jsonpath
import requests
if __name__=='__main__':
    resp=requests.post(url='http://43.133.227.52/api/login',
                       json={'username':'tester',
                             'password':'123456'}).json()
    token=jsonpath(resp,'$.token')
    print(token)