from flask import Flask, render_template, url_for, redirect, session
from authlib.integrations.flask_client import OAuth
from datetime import timedelta
import os, quickstart
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

app = Flask(__name__)
app.secret_key = 'secret key'
oauth = OAuth(app)
google = oauth.register(
    name='google',
    client_id="786418720345-k3mdlk7atdmncdpni9m22sodbacjda2e.apps.googleusercontent.com",
    client_secret="wJ-LWwx9RxA2aRtQeSgzzkUB",
    access_token_url='https://accounts.google.com/o/oauth2/token',
    access_token_params=None,
    authorize_url='https://accounts.google.com/o/oauth2/auth',
    authorize_params=None,
    api_base_url='https://www.googleapis.com/oauth2/v1/',
    client_kwargs={'scope': 'openid email profile'},
)


@app.route('/')
def index():
    # email = dict(session).get('email', None)
    info = dict(session)
    return info


@app.route('/login')
def login():
    redirect_uri = url_for('authorize', _external=True)
    return google.authorize_redirect(redirect_uri)

@app.route('/authorize')
def authorize():
    google = oauth.create_client('google')
    token = google.authorize_access_token()
    resp = google.get('userinfo')
    user_info = resp.json()
    session['email'] = user_info['email']

    creds = pickle.load(token)
    page_token = None
    service = build('calendar', 'v3', credentials=creds)
    while True:
        events = service.events().list(calendarId='primary', pageToken=page_token).execute()
        for event in events['items']:
            print(event['summary'])
        page_token = events.get('nextPageToken')
        if not page_token:
            break

    # return redirect('/')

@app.route('/logout')
def logout():
    for key in list(session.keys()):
        session.pop(key)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)