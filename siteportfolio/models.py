from siteportfolio import db
from datetime import datetime


class Produto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    produto = db.Column(db.String, unique=True, nullable=False)
    qtd = db.Column(db.Integer)
    categoria = db.Column(db.String, nullable=False)
    editor = db.Column(db.String, default='usuario_logado')
    data = db.Column(db.DateTime, default=datetime.utcnow())

# , db.CheckConstraint('qtd >= 0')



