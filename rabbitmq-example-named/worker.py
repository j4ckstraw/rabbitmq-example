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
channel.queue_declare(queue="task_queue",durable=True)
channel.basic_qos(prefetch_count = 1)
channel.basic_consume(callback,
                        queue='task_queue')

print("[x] Waiting for messages. To exit press CTRL+C")
channel.start_consuming()

