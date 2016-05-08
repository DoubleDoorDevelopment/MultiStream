# run this file when testing

from urllib import request
import json

from flask import Flask, jsonify, redirect
from flask.ext.sqlalchemy import SQLAlchemy

import config

app = Flask(__name__)
app.config.from_object('config')

@app.route('/')
def get_live_list():

    live_list = []

    streamers = [streamer for streamer in app.config['STREAMERS']]

    for streamer in streamers:
        with request.urlopen('https://api.twitch.tv/kraken/streams/%s' % streamer) as response:
            str_response = response.readall().decode('utf-8')
            obj = json.loads(str_response)
            if obj['stream'] is not None:
                live_list.append(streamer)

    new_url = 'http://multistre.am/%s' % ('/'.join(user for user in live_list))

    # return jsonify({'live': live_list})
    return redirect(new_url)


if __name__ == '__main__':
    app.run()