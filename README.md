# MultiStream

#### Version 1.1a1

Flask app for fetching if selected Twitch streams are live, and if so redirecting to multistre.am for the live users.

## Setup

Clone this repo, then `pip -r install requirements.txt`. To finish setup follow the config README instructions for 
editing the `__init__.py` config file.

## Usage

To run this app locally for testing purposes use the `run.py` file which enables debug. For server deployment I suggest
using [uWSGI](http://uwsgi-docs.readthedocs.io/en/latest/) and using it to run `app.py` directly.

<b>Note:</b> This version works completely different to version 1.0.
 
App runs a server that stores profiles containing lists of streams to query, and various filters including string
in title, game name, etc. These profiles can be created and accessed via the api. Comes with a web app that will get
streams for a given profile and redirect appropriately. Also provides convenient interface for creating new profiles.

## TODO:

 * Finish building API
 * Finish building web app
 * enable filtering of streams