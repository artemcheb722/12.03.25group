"""Basic connection example.
"""

import redis
import datetime

r = redis.Redis(
    host='redis-19340.c245.us-east-1-3.ec2.redns.redis-cloud.com',
    port=19340,
    decode_responses=True,
    username="default",
    password="ZdreayTB5XviQzaoBbGquFDULg7wf5qo",
)



# r.set('myKey', 'secret data')
#
#
# #
# #
# # r.lpush('myList', 'hweghdih')
# # r.rpush('myList', 'elem right', 565)
#
# data = r.lrange('myList', 0 , 5)
# print(data)
#
# r.delete('myList')

# r.hset('user:1234', mapping={'name': 'Alise', 'age': 56})
# r.expire('user:1234', 3500)

# r.set('myFavouriteCar', "BMW M4 Competition")
#
# r.set('MyPet', 'Dog')
# r.expire('MyPet', 7200)
# exat = datetime.datetime(year=2025, month=5, day=1, hour=2)
# time_delite = int(exat.timestamp())
# # r.lpush('MyProductsList', str(exat))
# r.expireat('MyProductsList', time_delite)

# r.hset('cake', mapping={'flour': 250, 'milk': 500})
# r.hset('cake', mapping={'sugar': 500})
# r.delete('cake')









