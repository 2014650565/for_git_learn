"""供 TDD 练习使用的简单计算器。"""

#new01

                  

def add(left, right):
    """返回两个数的和。"""
    return left + right


def subtract(left, right):
    """返回两个数的差。"""
    return left - right


def multiply(left, right):
    """返回两个数的积。"""
    return left * right


def divide(left, right):
    """返回两个数的商。"""
    return left / right


from jsonpath import jsonpath
import requests
if __name__=='__main__':
    resp=requests.post(url='http://43.133.227.52/api/login',
                       json={'username':'tester',
                             'password':'123456'}).json()
    token=jsonpath(resp,'$.token')
    print(token)


#test restore