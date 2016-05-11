# MultiStream

#### Version 1.0b1

Flask app for fetching if selected Twitch streams are live, and if so redirecting to multistre.am for the live users.

## Setup

Clone this repo, then `pip -r install requirements.txt`. To finish setup follow the config README instructions for 
editing the `__init__.py` config file.

## Usage

To run this app locally for testing purposes use the `run.py` file which enables debug. For server deployment I suggest
using [uWSGI](http://uwsgi-docs.readthedocs.io/en/latest/) and using it to run `app.py` directly.

To use this app, go to the url that you host this app on and it should redirect you to a multistre.am multistream for the 
streamers that you have specified in the config file. Optionally, streamers in the list can be filtered by the url e.g.:
`example.website.com` will redirect to a multistre.am url for all streamers in the list that are live; 
`example.website.com/d3` will redirect to a multistre.am url for all streamers in the list that are live that have the
   string `d3` in their stream title.
