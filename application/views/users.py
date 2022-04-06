from flask import request
from flask_restx import Resource, Namespace

from application.services.helpers.schemas import user
from application.container import users_service

users_ns = Namespace('users')
user_schema = user.UserSchema()
users_schema = user.UserSchema(many=True)


@users_ns.route('/<int:uid>/')
class UserView(Resource):

    def get(self, uid):
        return users_service.get_one(uid), 200

    def put(self, uid):
        """изменяем данные пользователя"""
        return users_service.update(uid, request.json), 200

    def delete(self, uid):
        """удаляем пользователя"""
        return users_service.delete(uid), 204


@users_ns.route('/')
class UsersView(Resource):

    def get(self):
        return users_service.get_all(), 200