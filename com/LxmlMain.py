# -*- coding: utf-8 -*-
from lxml import etree
import requests


text = '''
<html>
    <head><title>刘威</title></head>
</html>
'''

r = requests.get('http://www.baidu.com')
htmlContent = r.content

print htmlContent

myparser = etree.HTMLParser(encoding="utf-8")
html= etree.HTML(htmlContent,parser=myparser)
urls = html.xpath("/html/body/div[@id='wrapper']/div[@id='head']/div[@class='head_wrapper']/div[@id='u1']/a[@class='mnav'][1]/text()")

#urls = html.xpath("/html/head/title/text()")

#result = etree.tostring(urls)
for url in urls:
    print url.encode('utf-8')



