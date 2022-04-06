from application.dao.models.genre import Genre


class GenresDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        return self.session.query(Genre).all()

    def get_one(self, uid: int):
        return self.session.query(Genre).get(uid)