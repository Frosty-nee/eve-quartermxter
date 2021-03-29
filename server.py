#! python3
import eventlet
eventlet.monkey_patch()
import eventlet.wsgi

import os
import random
import string

import flask
from flask import request, session

import requests
from base64 import urlsafe_b64encode, urlsafe_b64decode as b64encode, b64decode
import urllib

import json
from authlib.jose import jwt

import swagger_client

import config
import db

app = flask.Flask(__name__)
app.secret_key = config.app_secret_key


esiconfig = swagger_client.Configuration()

@app.route('/')
def home():
    user = session['user']
    print(user)
    return flask.render_template('home.html')

@app.route('/login/director')
def director_login():
    payload = {
            'response_type': 'code',
            'client_id': config.esi_client_id,
            'scope': 'esi-assets.read_corporation_assets.v1',
            'state': ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase) for _ in range(16)),
            'redirect_uri': flask.url_for('login_callback', _external=True, _scheme='https')
    }
    return flask.redirect(''.join(('https://login.eveonline.com/v2/oauth/authorize?',urllib.parse.urlencode(payload))))

@app.route('/login/')
def login():
    payload = {
            'response_type': 'code',
            'client_id': config.esi_client_id,
            'scope': 'esi-characters.read_corporation_roles.v1',
            'state': ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase) for _ in range(16)),
            'redirect_uri': flask.url_for('login_callback', _external=True, _scheme='https')
    }

@app.route('/login/callback')
def login_callback():
    values = {t.split('=')[0]:t.split('=')[1] for t in request.full_path.split('?')[1].split('&')}
    data = {
        'grant_type':'authorization_code',
        'code': values['code'],
        }
    headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Host': 'login.eveonline.com',
            }
    r = requests.post('https://login.eveonline.com/v2/oauth/token',
            auth=(config.esi_client_id, config.esi_secret_key),
            data=data,
            headers=headers)

    data = json.loads(r.text)
    print(data)
    jwt_key = requests.get('https://login.eveonline.com/oauth/jwks')
    jwt_key = jwt_key.text

    session['user'] = jwt.decode(data['access_token'], jwt_key)

    return flask.redirect('/')

@app.route('/logout')
def logout():
    session['user'] = None
    return flask.redirect('/')

@app.route('/assets')
def assets():
    user = session.get('user')
    esiconfig.access_token = 'nothing sec'
    print(user)
    esi_assets_api = swagger_client.AssetsApi(swagger_client.ApiClient(esiconfig))
    if user == None:
        return flask.redirect(flask.url_for('login'))
    else:
        print(esi_assets_api.get_corporations_corporation_id_assets(98182803))

if __name__ == '__main__':
    if config.debug:
        app.run(port=config.port, debug=config.debug)
    else:
        listener = eventlet.listen((config.web_host, config.port))
        eventlet.wigi.server(listener, app)
