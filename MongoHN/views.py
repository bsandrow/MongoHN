from flask import session, render_template, redirect, g, flash, url_for
from flask.ext.login import login_required, login_user, logout_user, current_user
from wtforms.validators import ValidationError
from forms import LoginForm, RegistrationForm, SubmitStoryForm
from MongoHN import app, db, lm, models
from itertools import chain

import mongoengine.errors

@lm.user_loader
def load_user(id):
    return models.User.objects(id=id).first()

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

@app.route('/submit', methods=['GET','POST'])
@login_required
def submit():
    error_messages = None
    form = SubmitStoryForm()
    try:
        if form.validate_on_submit():
            story = form.create_story()
            return redirect(url_for('story', story_id=str(story.id)))
        elif form.errors:
            error_messages = chain(*form.errors.values())

    except ValidationError as ve:
        error_messages = [ ve.args[0] ]

    return render_template('submit.html', form=form, error_messages=error_messages)

@app.route('/story/<story_id>')
def story(story_id):
    try:
        story = models.Story.objects(id=story_id).first()
    except mongoengine.errors.ValidationError as e:
        story = None

    if story:
        return render_template('story.html', story=story)
    else:
        return render_template('story_not_found.html'), 404

