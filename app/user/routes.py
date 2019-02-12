from flask import Flask
from app.user import bp

@bp.route('/index2')
def index2():
	return "user"
