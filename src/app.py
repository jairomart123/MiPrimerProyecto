from re import S
from typing import TextIO
from click import password_option
from werkzeug.security import check_password_hash, generate_password_hash
from flask import Flask, render_template, request, redirect, url_for, flash, logging
from flask_mysqldb import MySQL
from functools import wraps
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager, login_user, logout_user, login_required
from conexionbd import obtener_conexion
from config import config
# Models:
from models.ModelUser import ModelUser

# Entities:
from models.entities.User import User

app = Flask(__name__)

csrf = CSRFProtect()
db = MySQL(app)
login_manager_app = LoginManager(app)


@login_manager_app.user_loader
def load_user(id):
    return ModelUser.get_by_id(db, id)


@app.route('/')
def index():
    return redirect(url_for('login'))

# EndPoint


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # print(request.form['username'])
        # print(request.form['password'])
        user = User(0, request.form['username'], request.form['password'])
        logged_user = ModelUser.login(db, user)
        if logged_user != None:
            if logged_user.password:
                login_user(logged_user)
                return redirect(url_for('home'))
            else:
                flash("Invalid password...")
                return render_template('auth/login.html')
        else:
            flash("User not found...")
            return render_template('auth/login.html')
    else:
        return render_template('auth/login.html')


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/registro')
def registro():
    return render_template('auth/registro.html')

# registro


@app.route('/newregistro', methods=['POST'])
def newregistro():
    if request.method == 'POST':
        username = request.form['username']
        Apellido = request.form['Apellido']
        fullname = request.form['Nombre']
        passw = request.form['password']
        Email = request.form['Email']
        Direccion = request.form['Direccion']
        Detalle = request.form['Detalle']
        Ciudad = request.form['Ciudad']
        Municipio = request.form['Municipio']
        Cgpostal = request.form['Cgpostal']
       # insertar datos
    password = passw
    passw = generate_password_hash(password)
    print(check_password_hash(passw, password))
    print(passw)

    conexion = obtener_conexion()

    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO user(username, password, fullname, Apellido, Email, Direccion, Detalle, Ciudad, Municipio, Cgpostal) VALUES (%s, %s, %s,%s,%s,%s,%s,%s,%s,%s)",
                        (username, passw, fullname, Apellido, Email, Direccion, Detalle, Ciudad, Municipio, Cgpostal))

        conexion.commit()
        conexion.close()
        flash('Gracias por registrarte')

    


    

    return redirect(url_for('login'))


@app.route('/protected')
@login_required
def protected():
    return "<h1>Esta es una vista protegida, solo para usuarios autenticados.</h1>"


def status_401(error):
    return redirect(url_for('login'))


def status_404(error):
    return "<h1>Página no encontrada</h1>", 404


if __name__ == '__main__':
    app.config.from_object(config['development'])
    csrf.init_app(app)
    app.register_error_handler(401, status_401)
    app.register_error_handler(404, status_404)
    app.run()
