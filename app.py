# run this file when testing

from urllib import request
import json

from flask import Flask, jsonify, redirect
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)


@app.route('/')
def get_live_list():

    live_list = []

    users = ['claycorp', 'dries007', 'drrosie', 'jjames5725']

    for user in users:
        with request.urlopen('https://api.twitch.tv/kraken/streams/%s' % user) as response:
            str_response = response.readall().decode('utf-8')
            obj = json.loads(str_response)
            if obj['stream'] is not None:
                live_list.append(user)

    new_url = 'http://multistre.am/%s' % ('/'.join(user for user in live_list))

    return redirect(new_url) #jsonify({'live': live_list})


if __name__ == '__main__':
    app.run()