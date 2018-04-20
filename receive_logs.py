#/usr/bin/env python3

import time
import pika

def callback(ch,method,properties,body):
    print("[x] Receive {}".format(body))
    time.sleep(body.count(b'.'))
    print("[x] Done")
    ch.basic_ack(delivery_tag = method.delivery_tag)

connection = pika.BlockingConnection()
channel = connection.channel()
channel.exchange_declare(exchange="logs",
                        exchange_type="fanout")
result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

channel.queue_bind(exchange="logs",
                    queue=queue_name)
channel.basic_qos(prefetch_count = 1)
channel.basic_consume(callback,
                        queue=queue_name)

print("[x] Waiting for messages. To exit press CTRL+C")
channel.start_consuming()

