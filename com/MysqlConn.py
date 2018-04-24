#!/usr/bin/python
# -*- coding: UTF-8 -*-

import MySQLdb
from AwsCollection import AwsCollection

def insertCollection(items):
    db = MySQLdb.connect("localhost", "root", "123456", "ocs_test", charset='utf8' )
    cursor = db.cursor()

    for collection in items:
        sql = "insert into aws_collection(id,title,url,comment_count,score,page,indexSeq,type) values ('%s','%s','%s','%d','%s','%d','%d','%s')" % \
          (collection.id,collection.title,collection.url,collection.comment,collection.score,collection.page,collection.indexSeq,collection.itemtype)

        try:
            cursor.execute(sql)
            db.commit()
        except:
            db.rollback()

    db.close()


def queryCollection():
    db = MySQLdb.connect("localhost", "root", "123456", "ocs_test", charset='utf8')
    cursor = db.cursor()

    items = []

    sql = "select * from aws_collection"
    cursor.execute(sql)
    results = cursor.fetchall()

    for item in results:
        id = item[0]
        title = item[1]
        url = item[2]
        comment = item[3]
        score = item[4]
        page = item[5]
        indexSeq = item[6]
        itemtype = item[7]
        collection = AwsCollection(id,title,url,comment,score,page,indexSeq,itemtype)
        items.append(collection)

    db.close()
    return items


def insertStatis(statis):
    db = MySQLdb.connect("localhost", "root", "123456", "ocs_test", charset='utf8')
    cursor = db.cursor()

    for item in statis:
        sql = "insert into aws_collection_statis(word,frequency,num) values ('%s','%d','%d')" % \
              (item.word, item.frequency, item.num)

        try:
            cursor.execute(sql)
            db.commit()
        except:
            db.rollback()

    db.close()
