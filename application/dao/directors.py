from application.dao.models.director import Director


class DirectorsDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        return self.session.query(Director).all()

    def get_one(self, uid: int):
        return self.session.query(Director).get(uid)
    
