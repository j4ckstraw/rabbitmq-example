#/usr/env/bin pythoin3

import pika
connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()
channel.queue_declare(queue="hello")

channel.basic_publish(exchange='',
                        routing_key = 'hello',
                        body = "hello world!")
print("[x]  Sent 'hello wolrd'")

connection.close()
