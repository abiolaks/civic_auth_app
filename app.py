import os
from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = os.environ.get('FLASK_SECRET', 'supersecret')
CIVIC_APP_ID = os.environ.get('CIVIC_APP_ID', 'demo_app_id')

PROJECTS = [
    {
        'title': 'Project Alpha',
        'description': 'A dummy project demonstrating Civic auth integration.'
    },
    {
        'title': 'Project Beta',
        'description': 'Another example project using fake data.'
    },
    {
        'title': 'Project Gamma',
        'description': 'Yet another project placeholder.'
    }
]

@app.route('/')
def index():
    return render_template('index.html', projects=PROJECTS)

@app.route('/login')
def login():
    return render_template('login.html', civic_app_id=CIVIC_APP_ID)

@app.route('/callback')
def callback():
    token = request.args.get('token')
    if token:
        session['token'] = token
    return redirect(url_for('profile'))

@app.route('/profile')
def profile():
    token = session.get('token')
    if not token:
        return redirect(url_for('login'))
    return render_template('profile.html', token=token)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
