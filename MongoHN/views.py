from flask import session, render_template, redirect, g, flash, url_for
from flask.ext.login import login_required, login_user, logout_user, current_user
from forms import LoginForm, RegistrationForm
from MongoHN import app, db, lm, models

@lm.user_loader
def load_user(id):
    return models.User.objects(username=id).first()

@app.before_request
def before_request():
        g.user = current_user

@app.route('/login', methods=['GET','POST'])
def login():
    if g.user is not None and g.user.is_authenticated():
        return redirect(url_for('index'))

    form = LoginForm()
    if form.validate_on_submit():
        login_user(form.user)
        flash("Logged in successfully.")
        return redirect(url_for('index'))

    return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/')
def index():
    import pprint
    pprint.pprint(session)
    return render_template('index.html', user=current_user)

@app.route('/register', methods=['GET','POST'])
def register():
    if g.user is not None and g.user.is_authenticated():
        return redirect(url_for('index'))

    form = RegistrationForm()
    if form.validate_on_submit():
        form.create_user()
        login_user(form.user)
        return redirect(url_for('index'))

    return render_template('register.html', form=form)
