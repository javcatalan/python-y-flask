from flask import Flask
from flask_socketio import SocketIO,emit

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from app import Config

app = Flask(__name__)
app.config['SECRET_KEY']= "secret!"


#todo configurando la aplicacion con la BD
app.config.from_object(Config)

#todo conectando mi aplicacion con mi BD
db=SQLAlchemy(app)

#app.config.from_object('configuration.DevConfig')

#configuaraciones
socketio = SocketIO(app)
db= SQLAlchemy(app)
migrate = Migrate(app,db)
login_manager = LoginManager(app)

#vistas importaciones
#from app.chat.controllers import chatBP
from app.user.controllers import userBp
#app.register_blueprint(userBp)
#app.register_blueprint(chatBP)





