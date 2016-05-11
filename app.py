import grequests

from flask import Flask, jsonify, redirect

app = Flask(__name__)
app.config.from_object('config')

@app.route('/')
@app.route('/<string:filter_>')
def get_live(filter_=''):

    live_list = []

    streamers = [streamer for streamer in app.config['STREAMERS']]
    # filter_ = app.config['FILTER']

    urls = [('https://api.twitch.tv/kraken/streams/%s' % streamer) for streamer in streamers]
    headers = {'Accept': 'application/vnd.twitchtv.v3+json',
               'Client-ID': app.config['CLIENT_ID']}
    requests = (grequests.get(url, headers=headers) for url in urls)
    response = grequests.map(requests, exception_handler=exception_handler)

    for index, value in enumerate(response):
        data = value.json()
        if data['stream'] is not None:
            if not filter_:
                live_list.append(streamers[index])
            elif filter_ in data['stream']['channel']['status']:
                live_list.append(streamers[index])

    new_url = 'http://multistre.am/%s' % ('/'.join(user for user in live_list))

    # return jsonify({'live': live_list})
    return redirect(new_url)

def exception_handler(request, exception):
        return 'Error processing request. Try refreshing.'


if __name__ == '__main__':
    app.run()