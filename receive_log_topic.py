#/usr/bin/env python3

import sys
import time
import pika

def callback(ch,method,properties,body):
    print("[x] Receive {}".format(body))
    time.sleep(body.count(b'.'))
    print("[x] Done")
    # ch.basic_ack(delivery_tag = method.delivery_tag)

connection = pika.BlockingConnection()
channel = connection.channel()
channel.exchange_declare(exchange="topic_logs",
                        exchange_type="topic")
result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

binding_keys = sys.argv[1:]
if not binding_keys:
    sys.stderr.write("Usage: %s [binding_keys]... \n" % sys.argv[0])
    sys.exit(1)

for binding_key in binding_keys:
    channel.queue_bind(exchange="topic_logs",
                    queue=queue_name,
                    routing_key = binding_key)


channel.basic_consume(callback,
                        queue=queue_name,
                        no_ack=True)

print("[x] Waiting for messages. To exit press CTRL+C")
channel.start_consuming()

