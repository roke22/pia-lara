from flask import Flask
from flask_login import LoginManager
from pialara import db
import os
import configparser

config = configparser.ConfigParser()
config.read(os.path.abspath(os.path.join(".ini")))


def create_app():
    # create and configure the app
    app = Flask(__name__)

    app.config['PIALARA_DB_URI'] = config['LOCAL']['PIALARA_DB_URI']
    app.config['PIALARA_DB_NAME'] = config['LOCAL']['PIALARA_DB_NAME']
    app.config['SECRET_KEY'] = config['LOCAL']['SECRET_KEY']

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    # Blueprints
    from pialara.blueprints import auth, syllabus, main, users
    app.register_blueprint(auth.bp)
    app.register_blueprint(syllabus.bp)
    app.register_blueprint(main.bp)
    app.register_blueprint(users.bp)

    @login_manager.user_loader
    def load_user(user_id):
        return db.get_user_by_id(user_id)

    # a simple page that says hello
    # @app.route('/hello')
    # def hello():
    #     return 'Hello, World!'

    return app
