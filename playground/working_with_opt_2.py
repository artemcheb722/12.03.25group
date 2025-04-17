import jwt
import datetime
import time


secret = 'dfpkpgfklg'

payload = {
    'my_name': 'Artem',
    'age': 14,
    'my_favourite_city': 'Kharkiv',
    'exp': datetime.datetime.now() + datetime.timedelta(seconds=10)
}

encode_jwt = jwt.encode(
    payload=payload,
    key=secret,
    algorithm='HS256'
)

print(encode_jwt)

time.sleep(15)
decoded = jwt.decode(
    encode_jwt,
    secret,
    algorithms=['HS256']
    )
print(decoded)
