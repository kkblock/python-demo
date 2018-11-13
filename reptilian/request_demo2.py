import requests

#会话对象
'''
会话对象让你能够跨请求保持某些参数。它也会在同一个 Session 实例发出的所有请求之间保持 cookie， 期间使用 urllib3 的 connection pooling 功能。
所以如果你向同一主机发送多个请求，底层的 TCP 连接将会被重用，从而带来显著的性能提升
'''
s = requests.session()

s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
r = s.get("http://httpbin.org/cookies")

print(r.text)
# '{"cookies": {"sessioncookie": "123456789"}}'

#会话也可用来为请求方法提供缺省数据。这是通过为会话对象的属性提供数据来实现的：
s = requests.Session()
s.auth = ('user', 'pass')
s.headers.update({'x-test': 'true'})

# both 'x-test' and 'x-test2' are sent
s.get('http://httpbin.org/headers', headers={'x-test2': 'true'})
print(s.headers)

#会话还可以用作前后文管理器：
with requests.Session() as s:
    s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')









