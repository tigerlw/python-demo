#!/usr/bin/python
# -*- coding: UTF-8 -*-

class AwsCollection:
    def __init__(self,id,title,url,comment,score,page,indexSeq,itemtype):
        self.id = id
        self.title = title
        self.url = url
        self.comment = comment
        self.score = score
        self.page = page
        self.indexSeq = indexSeq
        self.itemtype = itemtype

    def __str__(self):
        return "title:"+self.title+";url:"+self.url+";comment:"+str(self.comment)+";score:"+self.score

class StatisItem:
    def __init__(self,word,frequency,num):
        self.word = word
        self.frequency = frequency
        self.num = num
