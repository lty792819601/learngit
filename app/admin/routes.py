from app import app,db
from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.urls import url_parse
from app.admin import bp
from app.admin.forms import LoginForm, RegistrationForm,GameForm,BianjiGameForm
from app.models import User,Game
@bp.route('/')
@bp.route('/index')
@login_required
def index():
    games = Game.query.all()
    return render_template('index.html', title='Home', games=games)


@bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('admin.index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('admin.login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('admin.index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)


@bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('admin.index'))


@bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('admin.index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('admin.login'))
    return render_template('register.html', title='Register', form=form)

@bp.route('/editgame',methods=['GET','POST'])
@login_required
def editgame():
    form = GameForm()
    if form.validate_on_submit():
        game = Game(title=form.title.data, body=form.body.data) 
        db.session.add(game)
        db.session.commit()
        return redirect(url_for('admin.index'))
    return render_template('editgame.html',title='Editgame',form=form)

@bp.route('/bianjigame',methods=['GET','POST'])
@login_required
def bianjigame():
    gamename = request.args.get("title")
    gamebody = request.args.get("body")
    form = BianjiGameForm(gamename)
    if form.validate_on_submit():
        game = Game(title=form.title.data,body=form.body.data)
        db.session.commit()
        flash('ok')
        return redirect(url_for('admin.index'))
    elif request.method == 'GET':
        gamename = request.args.get("title")
        gamebody = request.args.get("body")
    
    return render_template('bianjigame.html',title='Bianji',form=form) 
