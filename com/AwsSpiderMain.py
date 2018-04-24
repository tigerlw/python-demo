import requests
import lxml
import re
from bs4 import BeautifulSoup
import Ngrams
from collections import OrderedDict
import collections
from AwsCollection import AwsCollection
import MysqlConn

output = []

awsCollection = []

session = requests.session()

headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5)AppleWebKit 537.36 (KHTML, like Gecko) Chrome",
           "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"}

url = "https://www.amazon.com/s/ref=nb_sb_noss_1?url=search-alias%3Daps&field-keywords=hair+wax"

rootUrl = "https://www.amazon.com"

r = session.get(url, headers=headers)
html = r.content

count = 0

while count < 1:

    print "page:"+str(count)

    soup = BeautifulSoup(html,'lxml')

    items = soup.findAll("li",{"id":re.compile("result_.")})

    for item in items:
        div = item.find("div",{"class":"a-row a-spacing-none a-spacing-top-mini"})
        print item.attrs["id"]

        tagA = div.find("a")

        title = tagA.attrs["title"]

        tmpOutput = Ngrams.getNgrams(title,4)

        output.extend(tmpOutput)

        print  title

        itemUrl = tagA.attrs["href"]

        if itemUrl.find(rootUrl) < 0:
            itemUrl = rootUrl + tagA.attrs["href"]

        print  itemUrl
        comment = item.find("a",{"class":"a-size-small a-link-normal a-text-normal"})

        if comment != None:
            commentCount = comment.get_text().replace(',','')
            print commentCount

        start = item.find("span",{"class":"a-icon-alt"})

        if start != None:
            score = start.get_text()
            print score

        collecion = AwsCollection(title,itemUrl,int(commentCount),score)

        awsCollection.append(collecion)



    nextUrl = soup.find("a",{"title":"Next Page"}).attrs["href"]

    pageUrl = "https://www.amazon.com"+nextUrl

    nextPage = session.get(pageUrl, headers=headers)
    html = nextPage.content
    count = count +1


#ngrams = OrderedDict(sorted(output.items(), key=lambda t: t[1], reverse=True))




#MysqlConn.insertCollection(awsCollection)






