#!/usr/bin/env python
import pika
import sys

credentials = pika.PlainCredentials('admin', 'admin')
connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='localhost',
    port=5672,
    virtual_host='/',
    credentials=credentials))

channel = connection.channel()

channel.exchange_declare(exchange='my_exchange',
                         exchange_type='fanout',
                         durable=True)

message = ' '.join(sys.argv[1:]) or "Tchêlinux"
channel.basic_publish(exchange='my_exchange',
                      routing_key='',
                      body=message)
print(" [x] Sent %r" % message)
connection.close()