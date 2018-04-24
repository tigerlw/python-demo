import requests
import lxml
import re
from bs4 import BeautifulSoup
r = requests.get('http://www.pythonscraping.com/pages/warandpeace.html')
html = r.content
soup = BeautifulSoup(html,'lxml')

adoc = soup.find_all("span", {"class":"green"})

#for doc in adoc :
   # print doc.get_text();




r = requests.get('http://www.pythonscraping.com/pages/page3.html')
html = r.content
soup = BeautifulSoup(html,'lxml')

#for sibling in soup.find("table",{"id":"giftList"}).tr.next_siblings:
    #print sibling


images = soup.findAll("img",{"src":re.compile("\.\./img/gifts/img.*\.jpg")})
for image in images:
    print(image["src"])
