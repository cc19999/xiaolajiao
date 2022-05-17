#!/usr/bin/env python
# --*--coding: utf-8 --*--
from pykafka import KafkaClient
from pykafka.topic import log
from pykafka.exceptions import MessageSizeTooLarge
from queue import Queue,Empty



# client = KafkaClient(hosts="1.12.247.227:9092")
# topic = client.topics['my_test']
#
# producer = topic.get_producer(delivery_reports=True)
# count = 0

#连接kafka客户端
kafka_client = KafkaClient(hosts="1.12.247.227:9092")
#获取topic
topic = kafka_client.topics["my_test"]
#获取生产者对象
produce = topic.get_producer()
#传数据必须是字节
for i in range(5):
    produce.produce(f"now_time_bytessdsdsds_{i}".encode("utf8"))
#手动关闭该生产者
produce.stop()


# =========================

# from pykafka import KafkaClient
# # from conf import KAFKA_HOSTS_LOCALHOST
# #连接kafka客户端
# kafka_client = KafkaClient(hosts='127.0.0.1:9092')
# #获取topic
# topic = kafka_client.topics["test"]
# #获取生产者对象
# produce = topic.get_producer()
# #传数据必须是字节
# for i in range(5):
#     produce.produce(f"now_time_bytessdsdsds_{i}".encode("utf8"))
# #手动关闭该生产者
# produce.stop()