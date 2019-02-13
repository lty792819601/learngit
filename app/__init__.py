from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
app = Flask(__name__)
app.config.from_object
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'
from app.admin import bp as admin_bp
app.register_blueprint(admin_bp)
from app.user import bp as user_bp
app.register_blueprint(user_bp)

