# Copyright 2016 Richard Campen
# All rights reserved
# This software is released under the Modified BSD license
# See LICENSE.txt for the full license documentation

"""Flask app for fetching if selected Twitch streams are live, and redirecting to multistre.am for the live streams.

MulstiStream version 1.0b2
==========================

For complete documentation see README.md.
"""

from flask import jsonify
import grequests

from multistream import app


@app.route('/api_v1/streams', methods=['GET'])
def get_live_streams():
    """Get currently live streamers."""

    streams_list = []

    streamers = [streamer for streamer in app.config['STREAMERS']]

    urls = [('https://api.twitch.tv/kraken/streams/%s' % streamer) for streamer in streamers]
    headers = {'Accept': 'application/vnd.twitchtv.v3+json',
               'Client-ID': app.config['CLIENT_ID']}
    requests = (grequests.get(url, headers=headers) for url in urls)
    response = grequests.map(requests)

    for index, value in enumerate(response):
        data = value.json()
        if data['stream'] is not None:
            streams_list.append(streamers[index])

    return jsonify({'streams': streams_list})