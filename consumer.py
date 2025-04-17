from work_with_Rabbit import get_connection
import pika
import json
from time import sleep

def process_new_message(channel, method, properties, body):
    try:
        log = json.loads(body.decode('utf-8'))
        print(f"Новий лог: {log['event']}, user_id: {log['user_id']}")
        sleep(1)
    except:
        pass


def consume_message(channel: pika.adapters.blocking_connection.BlockingChannel):
    QUEUE = 'logs'
    channel.basic_consume(
        queue=QUEUE,
        on_message_callback=process_new_message
    )

    channel.start_consuming()


def main():
    with get_connection() as connection:
        with connection.channel() as channel:
            consume_message(channel)


if __name__ == "__main__":
    main()