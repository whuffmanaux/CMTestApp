from app import db
from sqlalchemy import desc

ROLE_USER = 0
ROLE_ADMIN = 1

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64), index = True, unique = True)
    role = db.Column(db.SmallInteger, default = ROLE_USER)
    checkins = db.relationship('Checkin', backref = 'user', lazy = 'dynamic')

    def __repr__(self):
        return 'User(name=%r, role=%r)' % (self.name, self.role)

    def get_latest_checkins(self):
        return self.checkins.order_by(Checkin.timestamp.desc())

class Checkin(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    timestamp = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return 'Checkin(latitude=%r, longitude=%r, timestamp=%r)' % (self.latitude, self.longitude, self.timestamp)
