#!/usr/bin/python
# -*- coding: UTF-8 -*-

import MySQLdb
from AwsCollection import AwsCollection

def insertCollection(items):
    db = MySQLdb.connect("localhost", "root", "123456", "ocs_test", charset='utf8' )
    cursor = db.cursor()

    for collection in items:
        sql = "insert into aws_collection(title,url,comment_count,score) values ('%s','%s','%d','%s')" % \
          (collection.title,collection.url,collection.comment,collection.score)

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
        title = item[0]
        url = item[1]
        comment = item[2]
        score = item[3]
        collection = AwsCollection(title,url,comment,score)
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
