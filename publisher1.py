from work_with_Rabbit import get_connection
import pika.adapters.blocking_connection
from time import sleep


def produce_log(channel: pika.adapters.blocking_connection.BlockingChannel):
    QUEUE = 'logs'
    channel.queue_declare(queue=QUEUE)

    for item in range(100):
        message = f'{{"NewLog": "user_registered", "user_id": {item}}}'
        channel.basic_publish(
            exchange='',
            routing_key=QUEUE,
            body=message
        )


def main():
    with get_connection() as connection:
        with connection.channel() as channel:
            produce_log(channel)

if __name__ == "__main__":
    main()