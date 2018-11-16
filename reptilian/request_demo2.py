# -*- coding: utf-8 -*-
import json

import requests

#会话对象
from requests import Session, Request
from requests.auth import AuthBase


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

#获取header
r = requests.get('https://en.wikipedia.org/wiki/Main_Page')
print(r.headers)

#发送请求的header
print(r.request.headers)


s = Session()
req = Request('GET', 'http://www.baidu.com',
    data=None,
    headers=None
)
# prepped = req.prepare()
prepped = s.prepare_request(req)

# do something with prepped.body
# do something with prepped.headers

resp = s.send(prepped,
    stream=None,
    verify=None,
    proxies=None,
    cert=None,
    timeout=300
)

print(resp.status_code)

#以上的发送是没有状态的
#要获取一个带有状态的 PreparedRequest， 请用 Session.prepare_request() 取代 Request.prepare() 的调用，


'''
SSL,你可以为 verify 传入 CA_BUNDLE 文件的路径，或者包含可信任 CA 证书文件的文件夹路径,或者将其保持在会话中
'''
print(requests.get('https://github.com', verify=True))

# requests.get('https://github.com', verify='/path/to/certfile')

# s = requests.Session()
# s.verify = '/path/to/certfile'


#响应体内容工作流¶
'''
默认情况下，当你进行网络请求后，响应体会立即被下载。你可以通过 stream 参数覆盖这个行为，推迟下载响应体直到访问 Response.content 属性：
'''
tarball_url = 'https://github.com/kennethreitz/requests/tarball/master'
r = requests.get(tarball_url, stream=True)
print(r)
print(r.headers['Content-Type'])

#此时仅有响应头被下载下来了，连接保持打开状态，因此允许我们根据条件获取内容：
if r.headers['Content-Type'] == 'application/x-gzip':
    print(r.content)

#如果你发现你在使用 stream=True 的同时还在部分读取请求的 body（或者完全没有读取 body），那么你就应该考虑使用 with 语句发送请求，这样可以保证请求一定会被关闭：
with requests.get('http://httpbin.org/get', stream=True) as r:
    if r.headers['Content-Type'] == 'application/x-gzip':
        print(r.content)

#流式上传
'''
Requests支持流式上传，这允许你发送大的数据流或文件而无需先把它们读入内存。要使用流式上传，仅需为你的请求体提供一个类文件对象即可：
'''
# with open('massive-body') as f:
#     requests.post('http://some.url/streamed', data=f)

#事件挂钩
'''
可用的钩子:

response:
从一个请求产生的响应
你可以通过传递一个 {hook_name: callback_function} 字典给 hooks 请求参数为每个请求分配一个钩子函数：
'''
requests.get('http://httpbin.org', hooks=dict(response='http://httpbin.org'))

#自定义身份验证
'''
Requests 允许你使用自己指定的身份验证机制。
任何传递给请求方法的 auth 参数的可调用对象，在请求发出之前都有机会修改请求。
自定义的身份验证机制是作为 requests.auth.AuthBase 的子类来实现的，也非常容易定义。Requests 在 requests.auth 中提供了两种常见的的身份验证方案： HTTPBasicAuth 和 HTTPDigestAuth
'''

class PizzaAuth(AuthBase):
    """Attaches HTTP Pizza Authentication to the given Request object."""
    def __init__(self, username):
        # setup any auth-related data here
        self.username = username

    def __call__(self, r):
        # modify and return the request
        r.headers['X-Pizza'] = self.username
        return r

r = requests.get('http://www.baidu.com', auth=PizzaAuth('kenneth'))
print(r.url,r.headers)

#流式请求
'''
使用 Response.iter_lines() 你可以很方便地对流式 API （例如 Twitter 的流式 API ） 进行迭代。简单地设置 stream 为 True 便可以使用 iter_lines 对相应进行迭代
decode_unicode=True 提供一个回退编码方法,避免错误
'''
# r = requests.get('http://httpbin.org/stream/20', stream=True)
#
# for line in r.iter_lines(decode_unicode=True):
#
#     # filter out keep-alive new lines
#     if line:
#         decoded_line = line.decode('utf-8')
#         print(json.loads(decoded_line))


#代理
proxies = {
  "http": "http://127.0.0.1:1080"
}
r = requests.get("https://github.com/", proxies=proxies)
if r.status_code == requests.status_codes:
    print(r.content)
