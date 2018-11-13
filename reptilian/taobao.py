# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

#天猫商品地址
url = 'https://list.tmall.com/search_product.htm?q=%C8%FD%BC%FE%CC%D7&type=p&vmarket=&spm=875.7931836%2FB.a2227oh.d100&from=mallfp..pc_1_searchbutton'
r = requests.get(url=url)

responseText = r.text

soup = BeautifulSoup(responseText, 'html5lib')

print(soup.title.text)

#商品列表
divs = soup.select('div[class="product "]')
print(divs)