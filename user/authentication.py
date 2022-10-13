import jwt, datetime
from dateutil.relativedelta import relativedelta
from rest_framework import exceptions
from rest_framework.exceptions import AuthenticationFailed

def create_access_token(id):
    return jwt.encode({
        'user_id': id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1),
        'iat': datetime.datetime.utcnow()
    },  'access_secret', algorithm='HS256')

def access_token_exp(token):
    payload = jwt.decode(token, 'access_secret', algorithms='HS256')
    return payload['exp']
    

def decode_access_token(token):
    try:
        payload = jwt.decode(token, 'access_secret', algorithms='HS256')

        return payload['user_id']
    except:
        raise exceptions.AuthenticationFailed('unauthenticated')

def create_refresh_token(id):
    return jwt.encode({
        'user_id': id,
        'exp': datetime.datetime.utcnow() - relativedelta(months=1),
        'iat': datetime.datetime.utcnow()
    },  'refresh_secret', algorithm='HS256')

def decode_refresh_token(token):
    try:
        payload = jwt.decode(token, 'refresh_secret', algorithms='HS256')
        return payload['user_id']
    except:
        raise exceptions.AuthenticationFailed('unauthenticated')