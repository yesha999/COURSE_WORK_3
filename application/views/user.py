from flask import request
from flask_restx import Resource, Namespace

from application.services.helpers.decorators import user_required
from application.services.helpers.schemas import user
from application.container import users_service

user_ns = Namespace('user')
user_schema = user.UserSchema()
users_schema = user.UserSchema(many=True)


@user_ns.route('/')
class UserView(Resource):

    @user_required
    def get(self, email=''):
        """Получаем пользователя из email токена"""
        return users_service.get_by_email(email), 200

    @user_required
    def patch(self, email=''):
        """Берем из запроса возможные для изменения данные и отдаем в update"""
        req_json = request.json
        changed_values = {}
        if req_json.get('name'):
            changed_values['name'] = req_json.get('name')
        if req_json.get('surname'):
            changed_values['surname'] = req_json.get('surname')
        if req_json.get('favorite_genre'):
            changed_values['favorite_genre'] = req_json.get('favorite_genre')

        return users_service.update(email, changed_values), 200


@user_ns.route('/password/')
class PasswordMenu(Resource):
    @user_required
    def put(self, email=''):
        """Берем пароль, отдаем в сервис проверки пароля и хеширования"""
        req_json = request.json
        if req_json.get('password_1') and req_json.get('password_2'):
            return users_service.change_password(email, req_json.get('password_1'), req_json.get('password_2'))

        return "Не задано поле 'password_1' или 'password_2'"
