import os
import sys

os.environ['SPARK_HOME']="D:\learning\spark\spark-2.2.1-bin-hadoop2.7"
#os.environ['PYSPARK_SUBMIT_ARGS'] ="--packages org.apache.spark:spark-streaming-kafka-0-8_2.11:2.2.1" "pyspark-shell"
sys.path.append("D:\learning\spark\spark-2.2.1-bin-hadoop2.7\python")

from pyspark import SparkContext
from pyspark import SparkConf
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
import kafka
import json


offsets = []


def out_put(m):
    print(m)


def store_offset(rdd):
    global offsets
    offsets = rdd.offsetRanges()
    return rdd


def print_offset(rdd):
    for o in offsets:
        print "%s %s %s %s %s" % (o.topic, o.partition, o.fromOffset, o.untilOffset, o.untilOffset - o.fromOffset)


conf = SparkConf()
conf.setAppName("NetworkWordCount")
conf.setMaster("local[*]")
scontext = SparkContext(conf=conf)
stream_context = StreamingContext(scontext, 10)

zookeeper = "localhost:2181"


kvs = KafkaUtils.createDirectStream(stream_context, ["spark-streaming"], {"metadata.broker.list": "localhost:9192"})
lines = kvs.map(lambda x: x[1])
result = lines.flatMap(lambda line: line.split(" ")).map(lambda word: (word, 1)).reduceByKey(lambda x, y: x + y)
kvs.transform(store_offset, ).foreachRDD(print_offset)
result.pprint()
stream_context.start()

stream_context.awaitTermination()

