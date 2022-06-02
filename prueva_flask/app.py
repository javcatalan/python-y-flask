from flask import Flask,render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db=SQLAlchemy(app)
class Config(object):
    #todo conectado a la base de datos de MYSQL
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:cargamos2022@localhost/bdcargamos'
    SQLALCHEMY_TRACK_MODIFICATIONS = True

@app.route('/')
def Index():
    return render_template('index.html')

@app.route('/add_contact', methods=['POST'])
def add_contact():
    if request.method== 'POST':
        fulllname=request.form['fullname']
        phone=request.form['phone']
        email=request.form['email']
        print(fulllname,email,phone)
        return 'recibido'

@app.route('/edit')
def edit():
    return 'edit'

@app.route('/delete')
def delete():
    return 'delete'

if __name__ == '__main__':
    app.run(debug= True)
