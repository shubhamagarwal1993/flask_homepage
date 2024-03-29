from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Nikilesh'}
    return render_template('index.html', title='Home')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # Check for username and password
        if form.username.data == "" and form.password.data == "":
            return redirect(url_for('index'))
    return render_template('index.html', title='Sign In', form=form)
