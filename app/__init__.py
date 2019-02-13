from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] ='mysql+pymysql://root:zxc510626@127.0.0.1:3306/app?charset=utf8'
app.config['SECRET_KEY'] = "tse"
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'admin.login'
from app.admin import bp as admin_bp
app.register_blueprint(admin_bp,url_prefix='/admin')
from app.user import bp as user_bp
app.register_blueprint(user_bp,url_prefix='/user')

