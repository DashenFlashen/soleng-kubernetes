#!/usr/bin/env python
import time
import pika
import os
import sys
import requests

RABBIT_QUEUE = os.environ.get('RABBIT_QUEUE', 'default')
RABBIT_HOST = os.environ.get('RABBIT_HOST', '127.0.0.1')
RABBIT_PORT = os.environ.get('RABBIT_PORT', 5672)

APP_HOST = os.environ.get('APP_HOST', '127.0.0.1')
APP_PORT = os.environ.get('APP_PORT', 9000)


def main():
    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body)
        try:
            response_json = requests.get(f'http://{APP_HOST}:{APP_PORT}')
            print(f'Response json: {response_json.content}')
            channel.basic_ack(method.delivery_tag)
        except Exception as e:
            print(e)
            time.sleep(5)


    connection = pika.BlockingConnection(pika.ConnectionParameters(RABBIT_HOST, RABBIT_PORT))
    channel = connection.channel()
    channel.queue_declare(queue=RABBIT_QUEUE)
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue=RABBIT_QUEUE, on_message_callback=callback)

    print(' [*] Waiting for messages...........')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
