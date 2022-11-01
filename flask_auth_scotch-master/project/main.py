# main.py

from flask import Blueprint, render_template
from flask_login import login_required, current_user


main = Blueprint('main', __name__)

# Temos dois blueprints para as nossas rotas
# No blueprint principal teremos a página inicial com a rota '/' e a página de usuário com a rota '/profile'
# Se o usuário tentar acessar sem ter conta(ser autenticado) ele será encaminhado para a rota de login 

# Depois da página inicial, o usuário é encaminhado para a página do usuário
@main.route('/')
def index():
    return render_template('index.html')

@main.route('/profile')
@login_required #função para exigir que o usuário tenha login
def profile():
    return render_template('profile.html', name=current_user.name)

