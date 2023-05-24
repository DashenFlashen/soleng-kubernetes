#!/usr/bin/env python
import sys
import pika


host = 'localhost'
port = 5672
queue_name = 'subscriber_queue'


def put_on_queue(message: str = 'Hello World'):
    connection = pika.BlockingConnection(pika.ConnectionParameters(host, port=port))
    channel = connection.channel()
    channel.queue_declare(queue=queue_name)

    channel.basic_publish(exchange='', routing_key=queue_name, body=message)
    print(f" [x] Sent {message}'")
    connection.close()


if __name__ == '__main__':
    arguments = iter(sys.argv[1:])
    message = next(arguments, 'Hello World')
    number = next(arguments, 1)
    for _ in range(int(number)):
        put_on_queue(message)
