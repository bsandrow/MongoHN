from MongoHN import db

class User(db.Document):
    username = db.StringField(required=True)
    password = db.StringField(required=True)
    active = db.BooleanField(default=True)
    email = db.StringField(required=True)
    last_login = db.DateTimeField(required=False)

    def check_password(self, password):
        return self.password == password

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def get_id(self):
        return str(self.id)

    def is_anonymous(self):
        return False

    def __repr__(self):
        return "<User(%s,%s)>" % (self.username, self.email)
