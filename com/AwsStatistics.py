#!/usr/bin/python
# -*- coding: UTF-8 -*-


from AwsCollection import AwsCollection
from AwsCollection import StatisItem
import MysqlConn
import Ngrams
from collections import OrderedDict
import collections

items = MysqlConn.queryCollection()
output = []
statisItems = []

wordNum = 5

for item in items:
    tmpOutput = Ngrams.getNgrams(item.title, wordNum)
    output.extend(tmpOutput)


resultOutput = collections.Counter(output)

for item in resultOutput.items():
    print "key:"+item[0] + ";value:"+ str(item[1])
    statis = StatisItem(item[0],item[1],wordNum)
    statisItems.append(statis)

MysqlConn.insertStatis(statisItems)