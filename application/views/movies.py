from flask import request
from flask_restx import Resource, Namespace

from application.container import movies_service
from application.services.helpers.decorators import auth_required
from application.services.helpers.schemas import movie

movies_ns = Namespace('movies')
movie_schema = movie.MovieSchema()
movies_schema = movie.MovieSchema(many=True)


@movies_ns.route('/<int:uid>/')
class MovieView(Resource):

    @auth_required
    def get(self, uid):
        return movies_service.get_one(uid), 200


@movies_ns.route('/')
class MoviesView(Resource):

    @auth_required
    def get(self):
        filters = request.args
        if filters == {}:
            return movies_service.get_all(), 200

        return movies_service.get_by_filters(filters), 200