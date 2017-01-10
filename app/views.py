from flask import flash
from flask import render_template
from werkzeug.utils import redirect

from app import app
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    posts = [
        { 'author' : 'nik',
          'body' : 'What a busy day'},
        { 'author' : 'shiv',
          'body' : 'I am don'}
    ]
    user = {'nickname' : 'akg'}
    return render_template('index.html',
                           title='Home',
                           posts=posts,
                           user=user)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenId = %s and Remeber Me = %s' %
              (form.openid.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html',
                           title='Sign In',
                           form=form,
                           providers=app.config['OPENID_PROVIDERS'])