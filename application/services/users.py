from typing import Dict, Any

from application.dao.users import UsersDAO
from application.services.helpers.get_hash import get_hash
from application.services.helpers.schemas.user import UserSchema


class UsersService:

    def __init__(self, dao: UsersDAO, schema: UserSchema):
        self.dao = dao
        self.schema = schema

    def get_all(self):
        """Сериализуем всех юзеров"""
        return self.schema.dump(self.dao.get_all(), many=True)

    def get_one(self, uid: int):
        """Сериализуем 1 юзера"""
        return self.schema.dump(self.dao.get_one(uid))

    def get_by_email(self, email: str):
        """Сериализуем 1 юзера"""

        user = self.schema.dump(self.dao.get_by_email(email))
        user.pop('password')
        user.pop('id')
        return user

    def update(self, email: str, data: Dict[str, Any]):
        """Загружаем полученные данные, сериализуем их"""
        self.schema.dump(self.dao.update(email, self.schema.load(data)))
        return UsersService.get_by_email(self, email), 200


    def change_password(self, email: str, password_1, password_2):
        """Проверяем, хешируем пароль, отдаем в функцию update"""
        user = self.schema.dump(self.dao.get_by_email(email))
        hash_password_1 = get_hash(password_1)
        if hash_password_1 == user.get('password'):
            hash_password_2 = get_hash(password_2)
            data = {'password': hash_password_2}
            return UsersService.update(self, email, data)
        else:
            return 'Неверный пароль', 401

    def create(self, data: Dict[str, Any]):
        """Загружаем новые данные, хэшируем пароль, создаем запись, сериализуем ее"""

        hash_password = get_hash(data.get('password'))
        data['password'] = hash_password
        return self.schema.dump(self.dao.create(self.schema.load(data)))

    def delete(self, uid: int):
        """Удаляем запись"""
        return self.dao.delete(uid)
