from MongoHN import db
from mongoengine.queryset import queryset_manager

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

class Story(db.Document):
    title = db.StringField(required=True)
    url = db.StringField()
    text = db.StringField()
    date_posted = db.DateTimeField(required=True)

    @queryset_manager
    def newest_posts(doc_cls, queryset, page=1, stories_per_page=20):
        start = (page - 1) * stories_per_page
        end = page * stories_per_page + 1
        return queryset.order_by('-date_posted')[start:end]

    def __repr__(self):
        return "<Story(%s,%s,%s)>" % (self.id, self.title, self.date_posted)
