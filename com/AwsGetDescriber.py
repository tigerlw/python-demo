import requests
import lxml
import re
from bs4 import BeautifulSoup
import Ngrams
from collections import OrderedDict
import collections
from AwsCollection import AwsCollection
from AwsCollection import DescItem
import MysqlConn

keyword = "hair wax"
items = MysqlConn.queryCollection(keyword)

session = requests.session()
headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5)AppleWebKit 537.36 (KHTML, like Gecko) Chrome",
           "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"}

descItems = []

for item in items:
    url = item.url
    r = session.get(url, headers=headers)
    html = r.content
    soup = BeautifulSoup(html, 'lxml')
    listItem = soup.findAll("li", {"class": "showHiddenFeatureBullets"})

    descText = ""
    for desc in listItem:
        descContent = desc.find("span").get_text()
        descText = descText + descContent

    print item.id
    print descText

    descItem = DescItem(item.id,descText)
    descItems.append(descItem)


MysqlConn.insertDesc(descItems)
