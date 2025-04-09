import redis
import time


r = redis.Redis(
    host='redis-19340.c245.us-east-1-3.ec2.redns.redis-cloud.com',
    port=19340,
    decode_responses=True,
    username="default",
    password="ZdreayTB5XviQzaoBbGquFDULg7wf5qo",
)

while True:
    message = input()
    r.publish('school', message)
    print(message)

