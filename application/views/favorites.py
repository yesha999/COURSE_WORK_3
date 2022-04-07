from flask import request
from flask_restx import Resource, Namespace

from application.services.helpers.decorators import user_required
from application.services.helpers.schemas import favorite
from application.container import favorites_service, users_service, movies_service

favorites_ns = Namespace('favorites')
favorite_schema = favorite.FavoriteSchema()
favorites_schema = favorite.FavoriteSchema(many=True)


@favorites_ns.route('/movies/<int:movie_id>/')
class FavoriteMenu(Resource):

    @user_required
    def post(self, email, movie_id):
        user = users_service.get_by_email(email)
        user_id = user.get('id')
        for movie in movies_service.get_all():
            if movie['id'] == movie_id:
                return favorites_service.add_favorite(int(user_id), int(movie_id)), 200
        return 'Не найдено фильма с таким id', 401


    @user_required
    def delete(self, email, movie_id):
        user = users_service.get_by_email(email)
        user_id = user.get('id')
        for movie in movies_service.get_all():
            if movie['id'] == movie_id:
                return favorites_service.del_favorite(int(user_id), int(movie_id)), 200
        return 'Не найдено фильма с таким id', 401