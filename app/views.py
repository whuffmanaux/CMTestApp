from flask import render_template, request
from app import app, db
from models import User, Checkin
import datetime

@app.route('/')
@app.route('/index')
def index():
    users = db.session.query(User).all()
    return render_template('index.html', users=users)

@app.route('/checkin', methods = ['POST'])
def checkin():
    if not request.data == '':
        data = unicode(request.data).__str__().split(';')
    else:
        if len(request.form.keys()) == 1:
            data = unicode(request.form.keys()[0]).__str__().split(';')
        else:
            data = ''
    print data
    if not len(data)==3 or not (data[0]=='m' or data[0]=='c'):
        return unicode('invalid')
    name = 'carter'
    if data[0]=='m':
        name = 'mike'
    user = User.query.filter_by(name = name).first()
    if user is None:
        return unicode('invalid')
    try:
        lat = float(data[1])
        lon = float(data[2])
    except ValueError:
        return unicode('invalid')
    checkin = Checkin(latitude=lat, longitude=lon, timestamp=datetime.datetime.now(), user=user)
    db.session.add(checkin)
    db.session.commit()
    return unicode('got;it')

@app.route('/recent/<user>')
def recent(user):
    user = User.query.filter_by(name = user).first()
    if user is None:
        return unicode('invalid')
    checkin = user.get_latest_checkins().first()
    if checkin is None:
        return unicode('invalid')
    date = checkin.timestamp.date()
    time = checkin.timestamp.time()
    message = checkin.longitude.__str__()+';'+checkin.latitude.__str__()+';'+time.hour.__str__()+';'+time.minute.__str__()+';'+date.day.__str__()+';'+date.month.__str__()+';'+date.year.__str__()
    return unicode(message)
