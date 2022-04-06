import jwt
from flask import request
from flask_restx import abort

from application.constants import SECRET_HERE


def auth_required(func):
    """Проверяет наличие корректного токена"""

    def wrapper(*args, **kwargs):
        if 'Authorization' not in request.headers:
            abort(401)
        data = request.headers['Authorization']
        token = data.split(' ')[-1]
        try:
            decoded_token = jwt.decode(token, SECRET_HERE, 'HS256')
        except Exception as e:
            abort(401)

        if decoded_token['refresh_token']:
            abort(400)

        return func(*args, **kwargs)

    return wrapper


def admin_required(func):
    """Вначале проверяет наличие корректного токена и затем совпадение роли"""
    auth_required(func)

    def wrapper(*args, **kwargs):
        data = request.headers['Authorization']
        token = data.split(' ')[-1]
        decoded_token = jwt.decode(token, SECRET_HERE, 'HS256')
        if decoded_token['role'] != 'admin':
            abort(400, message='Недостаточно прав')
        return func(*args, **kwargs)

    return wrapper


def user_required(func):
    auth_required(func)

    def wrapper(*args, **kwargs):
        data = request.headers['Authorization']
        token = data.split(' ')[-1]
        decoded_token = jwt.decode(token, SECRET_HERE, 'HS256')
        email = decoded_token['email']
        return func(*args, email, **kwargs)

    return wrapper
