# -*- coding: utf-8 -*-

import json

import requests

url = 'http://www.baidu.com/s'
params = {'wd':'python'}

#指定url 同时传入参数,这里没有用url拼接,而是用的是默认的方式params,注意字典里值为 None 的键都不会被添加到 URL 的查询字符串里
#http://www.baidu.com/s?wd=python
r = requests.get(url=url,params=params)
print(r.url)

#也可以使用列表,http://www.baidu.com/s?wd=python&wd=python2
params = {'wd':['python','python2']}
r = requests.get(url=url,params=params)
print(r.url)

#获取响应内容
# print(r.text)

#获取编码
print(r.encoding)

#自己指定编码,这样再输出内容就是指定编码之后的内容了
# r.encoding = 'ISO8859-1'
# print(r.text)

#你也能以字节的方式访问请求响应体，对于非文本请求：
print(r.content)

#Requests 中也有一个内置的 JSON 解码器，助你处理 JSON 数据：
r = requests.get('https://api.github.com/events')
print(r.json())

#定制请求头
url = 'https://api.github.com/some/endpoint'
headers = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'}
r = requests.get(url, headers=headers)
print(r.headers)


#更加复杂的 POST 请求,只需简单地传递一个字典给 data 参数
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.post("http://httpbin.org/post", data=payload)
print(r.text)

#还可以为 data 参数传入一个元组列表。在表单中多个元素使用同一 key 的时候，这种方式尤其有效：
payload = (('key1', 'value1'), ('key1', 'value2'))
r = requests.post('http://httpbin.org/post', data=payload)
print(r.text)

#很多时候你想要发送的数据并非编码为表单形式的。如果你传递一个 string 而不是一个 dict，那么数据会被直接发布出去。
url = 'https://api.github.com/some/endpoint'
payload = {'some': 'data'}
r = requests.post(url, data=json.dumps(payload))
print(r.text)

#或者是传递json
url = 'https://api.github.com/some/endpoint'
payload = {'some': 'data'}
r = requests.post(url, json=payload)
print(r.text)

#POST一个多部分编码(Multipart-Encoded)的文件
url = 'http://httpbin.org/post'
files = {'file': open('/home/black/downloads/client.ovpn', 'rb')}
r = requests.post(url, files=files)
print(r.text)


#可以显式地设置文件名，文件类型和请求头：
url = 'http://httpbin.org/post'
files = {'file': ('client.ovpn', open('/home/black/downloads/client.ovpn', 'rb'), 'application/vnd.ms-excel', {'Expires': '0'})}
r = requests.post(url, files=files)
print(r.text)

#响应状态码
r = requests.get('http://httpbin.org/get')
print(r.status_code)
#为方便引用，Requests还附带了一个内置的状态码查询对象：
print(r.status_code == requests.codes.ok)

#如果发送了一个错误请求(一个 4XX 客户端错误，或者 5XX 服务器错误响应)，我们可以通过 Response.raise_for_status() 来抛出异常：
bad_r = requests.get('http://httpbin.org/status/404')
print(bad_r.status_code)
# bad_r.raise_for_status()

print(r.headers)


#Cookie 快速访问cookie内容
url = 'http://example.com/some/cookie/setting/url'
r = requests.get(url)
# print(r.cookies['example_cookie_name'])

#要想发送你的cookies到服务器，可以使用 cookies 参数：
url = 'http://httpbin.org/cookies'
cookies = dict(cookies_are='working')
r = requests.get(url, cookies=cookies)
print(r.text)


#Cookie 的返回对象为 RequestsCookieJar,它的行为和字典类似，但接口更为完整，适合跨域名跨路径使用。你还可以把 Cookie Jar 传到 Requests 中：
jar = requests.cookies.RequestsCookieJar()
jar.set('tasty_cookie', 'yum', domain='httpbin.org', path='/cookies')
jar.set('gross_cookie', 'blech', domain='httpbin.org', path='/elsewhere')
url = 'http://httpbin.org/cookies'
r = requests.get(url, cookies=jar)
print(r.text)

#重定向与请求历史 默认情况下，除了 HEAD, Requests 会自动处理所有重定向。例如，Github 将所有的 HTTP 请求重定向到 HTTPS：
r = requests.get('http://github.com')

#如果你使用的是GET、OPTIONS、POST、PUT、PATCH 或者 DELETE，那么你可以通过 allow_redirects 参数禁用重定向处理：
r = requests.get('http://github.com', allow_redirects=False)


#超时
requests.get('http://github.com', timeout=100)

'''
遇到网络问题（如：DNS 查询失败、拒绝连接等）时，Requests 会抛出一个 ConnectionError 异常。

如果 HTTP 请求返回了不成功的状态码， Response.raise_for_status() 会抛出一个 HTTPError 异常。

若请求超时，则抛出一个 Timeout 异常。

若请求超过了设定的最大重定向次数，则会抛出一个 TooManyRedirects 异常。

所有Requests显式抛出的异常都继承自 requests.exceptions.RequestException 。
'''





