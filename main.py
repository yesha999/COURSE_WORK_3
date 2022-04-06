from flask import Flask
from flask_restx import Api

from application.config import Config
from application.database import db
from application.views.auth import auth_ns
from application.views.movies import movies_ns
from application.views.genres import genres_ns
from application.views.directors import directors_ns
from application.views.user import user_ns
from application.views.users import users_ns


def create_app():
    """Создаем приложение"""
    app = Flask(__name__)
    app.config.from_object(Config)
    app.app_context().push()
    return app


def configure_app(app):
    """Конфигурируем приложение"""
    db.init_app(app)
    db.create_all()
    api = Api(app)
    api.add_namespace(movies_ns)
    api.add_namespace(genres_ns)
    api.add_namespace(directors_ns)
    api.add_namespace(auth_ns)
    api.add_namespace(users_ns)
    api.add_namespace(user_ns)


if __name__ == '__main__':
    """Запускаем приложение"""
    app_ = create_app()
    configure_app(app_)
    app_.run(host="localhost", port=10001, debug=True)
