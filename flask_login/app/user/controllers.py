from flask import  Blueprint, render_template, redirect, url_for
from werkzeug.security import generate_password_hash
from flask_login import login_user, current_user

from app.user.models import Users
from app.user.forms import RegisterForm
from app import db, login_manager

@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(user_id)

userBp = Blueprint('user',__name__)

@userBp.route('register', methods=('GET','POST'))
def register(): 

    print(current_user)

    form = RegisterForm(meta={'csrf':False})

    if form.validate_on_submit():
        if Users.query.filter_by(username=form.username.data).first():
            print("usuario dublicado")

        else:
            user =Users()
            user.name = form.name.data
            user.username = form.username.data
            user.password = generate_password_hash(form.password.data)
            user.email = form.email.data

            db.session.add(user)
            db.session.commit()

            login_user(user, remember=True)

            return redirect(url_for('user.register'))


    if form.errors:
        print(form.errors)

    return render_template('user/register.html',form=form)