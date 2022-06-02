from app import db

class Usuarios(db.Model):
    cod_grupo=db.column(db.String(4), primary_key= True)
    username=db.column(db.String(20))
    email =db.column(db.Sting(20))
    password=db.column(db.String(8))

