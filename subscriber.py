#!/usr/bin/env python
import pika

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

channel.queue_declare(queue='my_queue', durable=True)

channel.queue_bind(exchange='my_exchange',
                   queue='my_queue')

print(' [*] Waiting for messages. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print(" [x] %r" % body.decode('utf-8'))

channel.basic_consume(callback,
                      queue='my_queue',
                      no_ack=False)

channel.start_consuming()