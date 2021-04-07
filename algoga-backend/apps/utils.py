import datetime
import jwt
from django.conf import settings


def generate_access_token(email):

    access_token_payload = {
        'user_id': email,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, minutes=30),
        'iat': datetime.datetime.utcnow(),
    }
    access_token = jwt.encode(access_token_payload,
                              settings.SECRET_KEY, algorithm='HS256').decode('utf-8')
    return access_token

def email_token(email):

    access_token_payload = {
        'user_id': email,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, minutes=10),
        'iat': datetime.datetime.utcnow(),
    }
    access_token = jwt.encode(access_token_payload,
                              settings.SECRET_KEY, algorithm='HS256').decode('utf-8')
    return access_token
