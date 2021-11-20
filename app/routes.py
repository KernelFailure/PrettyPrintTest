from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'leon'}
    return render_template('tagTest.html', title='Home', user=user)
