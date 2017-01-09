from flask import render_template
from app import app

@app.route('/')
@app.route('/index.html')
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
