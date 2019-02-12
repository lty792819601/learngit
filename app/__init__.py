from flask import Flask
app = Flask(__name__)
from app.admin import bp as admin_bp
app.register_blueprint(admin_bp)
from app.user import bp as user_bp
app.register_blueprint(user_bp)
