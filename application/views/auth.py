import jwt
from flask import request
from flask_restx import Resource, Namespace

from application.container import auth_service, users_service

auth_ns = Namespace('auth')


@auth_ns.route('/login')
class LoginView(Resource):

    def post(self):
        """Получаем логин и пароль, идем создавать токены"""
        req_json = request.json

        email = req_json.get("email", None)
        password = req_json.get("password", None)

        if None in [email, password]:
            return "Не задан логин или пароль", 400

        tokens = auth_service.create_tokens(email=email, password=password)

        return tokens, 201

    def put(self):
        """Обновляем токены"""
        try:
            req_json = request.json
            refresh_token = req_json.get("refresh_token")
            tokens = auth_service.refresh_tokens(refresh_token)
        except jwt.ExpiredSignatureError as e:
            return "Токен истёк", 401
        except jwt.InvalidTokenError as e:
            return 'Неправильный токен', 401

        return tokens, 201


@auth_ns.route('/register/')
class RegisterView(Resource):
    def post(self):
        """Проверяем введенные данные, отдаем в сервис создания пользователя"""
        req_json = request.json
        if not req_json.get('email'):
            return 'Не задано поле email', 401

        if not req_json.get('password'):
            return 'Не задано поле password', 401

        for user in users_service.get_all():
            if user['email'] == req_json.get('email'):
                return 'Пользователь с таким email уже существует', 401

        return users_service.create(req_json), 201
