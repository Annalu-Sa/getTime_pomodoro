# init.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager 
#LoginManager library para utilização de sistema login
#SQLalchemy trabalha com banco de dados 

# init SQLAlchemy para usar em outras partes do código
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = '9OLWxND4o83j4K4iuopO'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from .models import User

    @login_manager.user_loader
    def load_user(user_id):
        # user_id é utilizada para consulta de user, já que é primary key da tabela de usuários
        return User.query.get(int(user_id))

    # blueprint para rota de autentificação no app
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprint para rota de não autentificação no app
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
