#!flask/bin/python
from app import db, models
from sqlalchemy import desc
import datetime
u = models.User(name='cat', role=models.ROLE_USER)
u2 = models.User(name='dog', role=models.ROLE_USER)
c1 = models.Checkin(latitude=1.0, longitude=2.0, timestamp=datetime.datetime.now(), user=u)
c2 = models.Checkin(latitude=2.0, longitude=2.0, timestamp=datetime.datetime.now(), user=u)
c3 = models.Checkin(latitude=3.0, longitude=3.0, timestamp=datetime.datetime.now(), user=u)
db.session.add(u)
db.session.add(u2)
db.session.add(c1)
db.session.add(c2)
db.session.add(c3)
db.session.commit()
print u.get_latest_checkins().all()
print u2.get_latest_checkins().all()
