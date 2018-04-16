#/usr/env/bin pythoin3

import sys
import pika

message = ' '.join(sys.argv[1:]) or "Hello world"
connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()
channel.queue_declare(queue="hello")

channel.basic_publish(exchange='',
                        routing_key = 'hello',
                        body = message)
print("[x]  Sent {}".format(message))

connection.close()
