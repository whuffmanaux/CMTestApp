#!flask/bin/python
from app import app
debug = False
if debug:
    app.run(debug=True)
else:
    app.run(debug=False, host='0.0.0.0')
