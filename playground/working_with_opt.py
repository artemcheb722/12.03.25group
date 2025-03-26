import jwt
import pyotp
import datetime

secret = 'dfpkpgfklg'

payload = {
    'my_name': 'Artem',
    'age': 14,
    'my_favourite_city': 'Kharkiv',
    'exp': datetime.datetime.now() + datetime.timedelta(seconds=1000)
}

encode_jwt = jwt.encode(
    payload=payload,
    key=secret,
    algorithm='HS256'
)

print(encode_jwt)

decoded = jwt.decode(
    encode_jwt,
    secret,
    algorithms=['HS256']
)

print(decoded)