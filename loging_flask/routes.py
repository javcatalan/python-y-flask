from flask import render_template, request
from loging_flask import app,db
from loging_flask.models import Usuarios

@app.route('/')
def index():
    template_name='index.html'
    usuarios=Usuarios.query.all()
    return render_template(template_name,usuarios=usuarios)