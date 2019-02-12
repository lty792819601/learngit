from app import app
from app.admin import bp
@bp.route('/index')
@bp.route('/')
def index():
	return "admin"
