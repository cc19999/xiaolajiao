#!/usr/bin/env python
# --*--coding: utf-8 --*--
from pykafka import KafkaClient
print('xxxxxxxx')

client = KafkaClient(hosts='1.12.247.227:9092')
# client = KafkaClient(hosts='127.0.0.1:9092')
print(client,'cccccc')
topic = client.topics['my_test']
print('当前所有的topic',client.topics)
print(topic)
consumer = topic.get_simple_consumer(
    consumer_group='my_group',
    auto_commit_enable=True,
    auto_commit_interval_ms=1,
    reset_offset_on_start=True
)


for message in consumer:
    print('kaishi')
    if message is not None:
        print('message>>',message.offset,message.value)
    else:
        print('message>> None')



# ======================

# from pykafka import KafkaClient
# # 设置客户端的连接信息
# client = KafkaClient(hosts="127.0.0.1:9092")
# topic = client.topics['test']
# # print(client.topics)
# # print(topic.latest_available_offsets())
# #consumer_group 与consumer_id值不能一样，不同group相互独立
# consumer  = topic.get_simple_consumer(
#     consumer_group='18',
#     auto_commit_enable=True,
#     auto_commit_interval_ms=1,
#     reset_offset_on_start=True
#     # consumer_id =1,
# )
#
#
# for message in consumer:
#     if message is not None:
#         print(message.offset, message.value)
#


