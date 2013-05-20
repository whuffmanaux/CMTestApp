#!flask/bin/python
from app import db, models
from sqlalchemy import desc
import datetime
u = models.User(name='carter', role=models.ROLE_USER)
u2 = models.User(name='mike', role=models.ROLE_USER)
c1 = models.Checkin(latitude=1.0, longitude=2.0, timestamp=datetime.datetime.now(), user=u)
c2 = models.Checkin(latitude=2.0, longitude=2.0, timestamp=datetime.datetime.now(), user=u2)
db.session.add(u)
db.session.add(u2)
db.session.add(c1)
db.session.add(c2)
db.session.commit()

