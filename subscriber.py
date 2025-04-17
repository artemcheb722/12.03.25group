import redis
r = redis.Redis(
    host='redis-19340.c245.us-east-1-3.ec2.redns.redis-cloud.com',
    port=19340,
    decode_responses=True,
    username="default",
    password="ZdreayTB5XviQzaoBbGquFDULg7wf5qo",
)

pubsub = r.pubsub()
pubsub.subscribe('school')



def save_message(message):
    if "контрольная работа" in message:
        r.lpush('messages', message)


for message in pubsub.listen():
    if message['type'] == 'message':
        data = message['data']
        print(data)
        save_message(data)