import sqlalchemy
from . import db

class User():
    __versioned__ = {'strategy': 'subquery'}
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=True)
    apellido = db.Column(db.String(512), nullable=True)




    def serialize(self):
        d = dict()
        d["id"] = self.id
        d["nombre"] = self.nombre
        d["apellido"] = self.apellido
        return d




