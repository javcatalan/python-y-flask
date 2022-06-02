from flask import Config, Flask
from loging_flask import config
from flask_sqlalchemy import SQLAlchemy

#todo creando la aplicacion 

app= Flask(__name__)

app.config.object(Config)

db=SQLAlchemy(app)

from loging_flask import routes, models
