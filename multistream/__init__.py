# Copyright 2016 Richard Campen
# All rights reserved
# This software is released under the Modified BSD license
# See LICENSE.txt for the full license documentation

"""Flask app for fetching if selected Twitch streams are live, and redirecting to multistre.am for the live streams.

MulstiStream version 1.0b2
==========================

For complete documentation see README.md.
"""

from flask import Flask

app = Flask(__name__)
app.config.from_object('config')

from multistream import views, api