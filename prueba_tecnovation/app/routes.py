from flask import jsonify, render_template,request,redirect,make_response
from app import app,db
from app.models import Usuarios
from app.serializer import Usuario_schema,Usuarios_schema

@app.route('/')
def index():
    cod_usuario=Usuarios.query.all()
    template_name='index.html'
    return render_template(template_name,grupos=cod_usuario)


@app.route('/agregar', methods=['POST'])
def agregar():
    cod_usuario=request.json['cod_usuario']
    email=request.json['email']
    new_usuario=Usuarios(cod_usuario,email)
    db.session.add(new_usuario)
    db.session.commit()
    result=Usuario_schema.dum(new_usuario)
    data={
        'message':'se agrego con exito',
        'status':200,
        'data':'result'
    }
    return make_response(jsonify(data))

    # if request.method == 'POST':
    #     form=request.form
    #     cod_usuario=form.get('cod_usuario')
    #     email=form.get('email')
    #     if not cod_usuario or email:
    #         grupos=Usuarios(cod_usuario=cod_usuario,email=email)
    #         db.session.add(grupos)
    #         db.session.commit()
    #         return redirect('/')
    #     return 'done'

@app.route('/eliminar/<int:id>')
def eliminar(id):
    if not id or id !=0:
        grupo=Usuarios.query.get(id)
        if grupo:
            db.session.delete(grupo)
            db.session.commit()
            return redirect('/')
        return 'done'

@app.route('/actualizar/<int:id>')
def actualizar(id):
    template_name='actualizar.html'
    if not id or id !=0:
        grupo=Usuarios.query.get(id)
        if grupo:
            return render_template(template_name,grupo=grupo)
        return 'done'




