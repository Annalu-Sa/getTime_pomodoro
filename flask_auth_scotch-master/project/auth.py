# auth.py
# Classe para criar páginas de web que apenas usuários autenticados conseguem acessar, organização e manutenção 


from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required
from .models import User
from . import db

auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    return render_template('login.html')

# Página de login, pedindo o email e a senha do usuário:
@auth.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(email=email).first()

    # Checar se o usuário de fato existe
    # Pegar a senha fornecida pelo usuário, fazer um hash e comparar
    # Ela com a senha com hash no banco de dados
    if not user or not check_password_hash(user.password, password): 
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login')) # if user doesn't exist or password is wrong, reload the page

    # Se a condicional acima for satisfeita, então sabemos que o usuário tem as credenciais corretas
    login_user(user, remember=remember)
    return redirect(url_for('main.profile'))

# Não tem conta -> Cadastrar o usuário
@auth.route('/signup')
def signup():
    return render_template('signup.html')

@auth.route('/signup', methods=['POST'])
def signup_post():

    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')

    user = User.query.filter_by(email=email).first() 
    # Se isso retornar um usu[ario, então o email já existe no Banco de Dados

    if user: 
        # Se um usuário existente é encontrado, 
        # Então o usuário criando a conta será redirecionado de volta para a página de signup   
        flash('Email address already exists')
        return redirect(url_for('auth.signup'))

    # Cria um novo novo usuário com o cadastramento recém realizado
    new_user = User(email=email, name=name, password=generate_password_hash(password, method='sha256'))

    # Adiciona o novo usuário ao Banco de Dados
    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('auth.login'))

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))
