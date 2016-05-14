# Copyright 2016 Richard Campen
# All rights reserved
# This software is released under the Modified BSD license
# See LICENSE.txt for the full license documentation

"""Flask app for fetching if selected Twitch streams are live, and redirecting to multistre.am for the live streams.

MulstiStream version 1.0b2
==========================

For complete documentation see README.md.
"""

from flask import render_template, flash, redirect, request, jsonify, url_for
import requests

from multistream import app, api

@app.route('/')
@app.route('/index.html')
def generate_url():

    return 'hi' #render_template('index.html')