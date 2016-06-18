# MultiStream

#### Version 1.0b4

Flask app for fetching if selected Twitch streams are live, and if so redirecting to multistre.am for the live users.

## Setup

Clone this repo, then `pip -r install requirements.txt`. To finish setup follow the config README instructions for 
editing the `__init__.py` config file.

## Usage

To run this app locally for testing purposes use the `run.py` file which enables debug. For server deployment I suggest
using [uWSGI](http://uwsgi-docs.readthedocs.io/en/latest/) and using it to run `app.py` directly.

To use this app, go to the url that you host this app on and it should redirect you to a multistre.am multistream for the 
streamers that you have specified in the config file. Optionally, streamers in the list can be filtered (case insensitive):

* `example.url/substring` will filter by streams containing the substring in their status. This is an alias for the
advanced filtering option by status below.

For advanced filtering:

* `example.url/status/substring` will filter by streams containing the substring in their status
* `example.url/game/string` will filter by streams whose game matches the string exactly

Both these options can be aliased by their first letters so `example.url/s/substring` and `example.url/g/string`.
