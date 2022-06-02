class Config(object):
    #todo conectado a la base de datos de MYSQL
   
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgresql:cargamos2022@localhost:Users'
    SQLALCHEMY_TRACK_MODIFICATIONS = True

#pip install psycopg2-binary