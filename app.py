# Copyright 2016 Richard Campen
# All rights reserved
# This software is released under the Modified BSD license
# See LICENSE.txt for the full license documentation

"""Flask app for fetching if selected Twitch streams are live, and redirecting to multistre.am for the live streams.

MultiStream version 1.0b4
==========================

For complete documentation see README.md.
"""

import grequests

from flask import Flask, jsonify, redirect

app = Flask(__name__)
app.config.from_object('config')

@app.route('/', methods=['GET'])
def get_all_live():

    live_list = []

    streamers = [streamer for streamer in app.config['STREAMERS']]

    urls = [('https://api.twitch.tv/kraken/streams/%s' % streamer) for streamer in streamers]
    headers = {'Accept': 'application/vnd.twitchtv.v3+json',
               'Client-ID': app.config['CLIENT_ID']}
    requests = (grequests.get(url, headers=headers) for url in urls)
    response = grequests.map(requests, exception_handler=exception_handler)

    for index, value in enumerate(response):
        data = value.json()
        if data['stream'] is not None:
            live_list.append(streamers[index])

    new_url = 'http://multistre.am/%s' % ('/'.join(user for user in live_list))

    return redirect(new_url, code=303)


@app.route('/<string:category>/<string:query>', methods=['GET'])
@app.route('/<string:query>', methods=['GET'])
def redirect_with_filter(category='', query=''):
    """Redirects to a multistre.am URL based on filter properties.

    Arguments:
        category:   (str) category by which to filter, e.g. status, game, profile
        query:      (str) filter to use [OPTIONAL]

    If no category argument is given the default behavior is to query by streamers status.
    """

    category_dict = {'status': filter_by_status,
                     's': filter_by_status,
                     'game': filter_by_game,
                     'g': filter_by_game}

    if not category:
        # TODO: do something more useful here
        redirect_url = filter_by_status(query)
        return 'redirect url: %s' % redirect_url

    if category in category_dict.keys():
        redirect_url = category_dict[category](query)
        # return 'redirect url: %s' % redirect_url
        return redirect(redirect_url, code=303)

    return 'default\ncategory: %s\nquery: %s' % (category, query)


def exception_handler(request, exception):
    return 'Error processing request. Try refreshing.'


def filter_by_status(status_query):
    """Filter default streamer list by substring in status."""

    live_list = []

    streamers = [streamer for streamer in app.config['STREAMERS']]

    urls = [('https://api.twitch.tv/kraken/streams/%s' % streamer) for streamer in streamers]
    headers = {'Accept': 'application/vnd.twitchtv.v3+json',
               'Client-ID': app.config['CLIENT_ID']}
    requests = (grequests.get(url, headers=headers) for url in urls)
    response = grequests.map(requests, exception_handler=exception_handler)

    for index, value in enumerate(response):
        data = value.json()
        if data['stream'] is not None:
            if status_query.lower() in data['stream']['channel']['status'].lower():
                live_list.append(streamers[index])

    new_url = 'http://multistre.am/%s' % ('/'.join(user for user in live_list))

    return new_url


def filter_by_game(game_query):
    """Filter default streamer list by exact matching game name."""

    live_list = []

    streamers = [streamer for streamer in app.config['STREAMERS']]

    urls = [('https://api.twitch.tv/kraken/streams/%s' % streamer) for streamer in streamers]
    headers = {'Accept': 'application/vnd.twitchtv.v3+json',
               'Client-ID': app.config['CLIENT_ID']}
    requests = (grequests.get(url, headers=headers) for url in urls)
    response = grequests.map(requests, exception_handler=exception_handler)

    for index, value in enumerate(response):
        data = value.json()
        if data['stream'] is not None:
            if game_query.lower() == data['stream']['channel']['game'].lower():
                live_list.append(streamers[index])

    new_url = 'http://multistre.am/%s' % ('/'.join(user for user in live_list))

    return new_url
