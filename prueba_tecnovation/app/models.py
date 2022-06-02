from app import db

# class Grupos(db.Model):
#     codgrupo=db.Column(db.Integer,primary_key=True)
#     nombre_grupo=db.Column(db.String(50))
#     estado=db.Column(db.Integer)


class Usuarios(db.Model):
    cod_usuario=db.Column(db.String(4),primary_key=True,autoincrement=True)#
    username=db.Column(db.String(20))#
    email=db.Column(db.String(20))
    # password=db.Column(db.String(8))#password

    def __init__(self,cod_usuario,username,email):
        self.cod_usuario=cod_usuario
        self.username=username 
        self.email=email