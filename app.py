# run this file when testing

import requests

from flask import Flask, jsonify, redirect

app = Flask(__name__)
app.config.from_object('config')

@app.route('/')
def get_live():

    live_list = []

    streamers = [streamer for streamer in app.config['STREAMERS']]

    for streamer in streamers:
        url = 'https://api.twitch.tv/kraken/streams/%s' % streamer
        headers = {'Accept': 'application/vnd.twitchtv.v3+json'}
        r = requests.get(url, headers)
        data = r.json()

        if data['stream'] is not None:
            filter_ = app.config['FILTER']
            if filter_ is None:
                live_list.append(streamer)
            else:
                if filter_ in data['stream']['channel']['status']:
                    live_list.append(streamer)


    new_url = 'http://multistre.am/%s' % ('/'.join(user for user in live_list))

    # return jsonify({'live': live_list})
    return redirect(new_url)


if __name__ == '__main__':
    app.run()