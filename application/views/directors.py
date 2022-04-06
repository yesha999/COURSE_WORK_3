from flask_restx import Resource, Namespace

from application.container import directors_service
from application.services.helpers.decorators import auth_required, admin_required
from application.services.helpers.schemas import director

directors_ns = Namespace('directors')
director_schema = director.DirectorSchema()
directors_schema = director.DirectorSchema(many=True)


@directors_ns.route('/<int:uid>/')
class DirectorView(Resource):

    @auth_required
    def get(self, uid):
        return directors_service.get_one(uid), 200


@directors_ns.route('/')
class MoviesView(Resource):

    @auth_required
    def get(self):
        return directors_service.get_all()
