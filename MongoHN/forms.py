""" MongoHN.forms - WTForms used by MongoHN """

from MongoHN.models import User
from flask.ext.wtf import Form
from wtforms import SubmitField, TextField, BooleanField, PasswordField
from wtforms.validators import Required, DataRequired

class LoginForm(Form):
    username = TextField('Username', validators = [ Required() ])
    password = PasswordField('Password', validators = [ Required() ])
    remember_me = BooleanField('remember_me', default = False)
    submit = SubmitField('Login')

    def validate(self):
        rv = Form.validate(self)
        if not rv:
            return False

        user = User.objects(username=self.username.data).first()

        if user is None:
            self.username.errors.append('Unknown username')
            return False

        if not user.check_password(self.password.data):
            self.password.errors.append('Invalid password')
            return False

        self.user = user
        return True

class RegistrationForm(Form):
    username = TextField('Username', validators=[ DataRequired() ])
    password = PasswordField('Password', validators=[ DataRequired() ])
    email = TextField('Email', validators=[ DataRequired() ])
    submit = SubmitField('Register', validators=[ Required() ])

    def validate_username(form, field):
        if User.objects(username=field.data).first():
            raise ValueError("Username already exists.")

    def create_user(self):
        user = User()
        user.username = self.username.data
        user.password = self.password.data
        user.email = self.email.data
        user.save()
        self.user = user

#
