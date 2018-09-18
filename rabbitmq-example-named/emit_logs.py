#/usr/env/bin pythoin3

import sys
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()
channel.exchange_declare(exchange="logs",exchange_type="fanout")

message = ' '.join(sys.argv[1:]) or "Hello world"
channel.basic_publish(exchange='logs',
                        routing_key = '',
                        body = message)
print("[x]  Sent {}".format(message))

connection.close()
