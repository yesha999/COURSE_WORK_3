from typing import Dict, Any

from application.dao.models.user import User


class UsersDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        """Получаем всех юзеров (несериализованные)"""
        return self.session.query(User).all()

    def get_one(self, uid: int):
        """Получаем 1 юзера (несериализованный)"""
        return self.session.query(User).get(uid)

    def update(self, email: str, data: Dict[str, Any]):
        """Изменяем данные 1 юзера, возвращаем измененного"""
        self.session.query(User).filter(User.email == email).update(data)
        self.session.commit()
        return self.get_by_email(email)

    def create(self, data: Dict[str, Any]):
        """Добавляем нового юзера, получаем его же"""
        new_user = User(**data)
        self.session.add(new_user)
        self.session.commit()

        return new_user

    def delete(self, uid: int):
        delete_user = self.get_one(uid)
        self.session.delete(delete_user)
        self.session.commit()
        return ''

    def get_by_email(self, email: str):
        """Получаем 1 юзера по имени (несериализованный)"""
        return self.session.query(User).filter(User.email == email).first()