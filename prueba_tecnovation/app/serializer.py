from app import app

from app.models import Usuarios
#todo la libreria marshmallow me permite serializar
#todo los objetos de mi clase a un formato json
from flask_marshmallow import Marshmallow

ma= Marshmallow(app)


class UsuarioSerializer(ma.SQLAlchemyAutoSchema):
    class Meta:
        model=Usuarios
        fields=('cod_grupo','username','email')
        
#todo lo utilizare cuando deseo mostrar solo un registro        
Usuario_schema=UsuarioSerializer()
#todo lo utilizare cuando deseo mostrar varios
Usuarios_schema=UsuarioSerializer(many=True)