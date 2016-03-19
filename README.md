DjangoCon US 2016
=================

DjangoCon US 2016 is built on top of [Pinax Symposion](https://github.com/pinax/symposion) and [PinaxCon](https://github.com/pinax/PinaxCon). With our changes, your mileage may vary.


Code of Conduct
---------------

As a contributor, you can help us keep the Django community open and inclusive.
Please read and follow our [Code of Conduct](https://www.djangoproject.com/conduct/).


Getting Started
----------------

Make sure you are using a virtual environment of some sort (e.g. `virtualenv` or
`pyenv`).

Create a database (defaults to Postgres):

    $ createdb djangocon2016

Install requirements:

    $ pip install -r requirements.txt

Create a local settings file and set your `DJANGO_SETTINGS_MODULE` to use it:

    $ cp djangocon/settings/local.py.example djangocon/settings/local.py

    $ export DJANGO_SETTINGS_MODULE=djangocon.settings.local

Sync models to database:

    $ ./manage.py migrate

Load default fixtures into database:

    $ ./manage.py loaddata fixtures/*

Create a superuser account to access the admin:

    $ ./manage.py createsuperuser

Start the web server:

    $ ./manage.py runserver


Static files
------------

The static file compilation is done with Node dependencies. On a Mac install
node via Homebrew:

    $ brew install node

Install all node dev dependencies:

    $ npm install

To compile all static files simply run:

    $ make all

#### Static files during development

You can watch for changes of CSS and JS files and have them re-compiled
on-the-fly. Run each command in a separate shell.

    $ make js watch=1
    $ make css watch=1

#### How static files are treated

* All client/browser related files are stored in `client/`.
* Static files which don't need processing are in `client/assets`.
* CSS and JS  are compiled into the `build/` folder using a `make` command.
* Django's `collectstatic` takes everything from the `build/` folder plus
  the "classic" application static files and puts them in `<venv>/var/static/`.
  This is also the folder we serve with the webserver.

For CSS we use a factory of: Node-Sass for CSS compilation + autoprefixer.

For JS we use browserify to collect all dependencies, from `client/js` as well
as from the `node_modules` into one file. We transform that with Babel from ES6
to ES5 for compatibility reasons. We compress that with uglify.


Contributors
---------------

Thanks goes to these wonderful people ([emoji key](#emoji-key)) (semi-ordered by contribution date):

Contributor | Contributions
:---: | :---:
[![Mark Wirblich](https://avatars.githubusercontent.com/u/11863?v=3&s=100)<br />Mark Wirblich](https://github.com/mightym) | [🎨💻📖](https://github.com/djangocon/2016.djangocon.us/commits?author=mightym)
[![Jeff Triplett](https://avatars.githubusercontent.com/u/50527?v=3&s=100)<br />Jeff Triplett](https://github.com/jefftriplett) | [💻📖](https://github.com/djangocon/2016.djangocon.us/commits?author=jefftriplett)
[![Katherine Michel](https://avatars.githubusercontent.com/u/4193054?v=3&s=100)<br />Katherine Michel](https://github.com/KatherineMichel) | [📖❓](https://github.com/djangocon/2016.djangocon.us/commits?author=KatherineMichel)
[![Peter Baumgartner](https://avatars.githubusercontent.com/u/319156?v=3&s=100)<br />Peter Baumgartner](https://github.com/ipmb) | [💻📖](https://github.com/djangocon/2016.djangocon.us/commits?author=ipmb)
[![Patrick Altman](https://avatars.githubusercontent.com/u/1192?v=3&s=100)<br />Patrick Altman](https://github.com/paltman) | [💻📖](https://github.com/djangocon/2016.djangocon.us/commits?author=paltman)
[![Anna Ossowski](https://avatars.githubusercontent.com/u/8700795?v=3&s=100)<br />Anna Ossowski](https://github.com/ossanna16) | [📖](https://github.com/djangocon/2016.djangocon.us/commits?author=ossanna16)
[![Lacey Williams Henschel](https://avatars.githubusercontent.com/u/2286304?v=3&s=100)<br />Lacey Williams Henschel](https://github.com/williln) | [📖❓](https://github.com/djangocon/2016.djangocon.us/commits?author=williln)
[![Sara D Gore](https://avatars.githubusercontent.com/u/2285473?v=3&s=100)<br />Sara D Gore](https://github.com/SaraDGore) | [📖❓](https://github.com/djangocon/2016.djangocon.us/commits?author=SaraDGore)
[![Andrew Pinkham](https://avatars.githubusercontent.com/u/2659203?v=3&s=100)<br />Andrew Pinkham](https://github.com/jambonrose) | [📖❓](https://github.com/djangocon/2016.djangocon.us/commits?author=jambonrose)
[![Brian Rosner](https://avatars.githubusercontent.com/u/124?v=3&s=100)<br />Brian Rosner](https://github.com/brosner) | [💻](https://github.com/djangocon/2016.djangocon.us/commits?author=brosner)
[![Kojo Idrissa](https://avatars.githubusercontent.com/u/5251109?v=3&s=100)<br />Kojo Idrissa](https://github.com/kojoidrissa) | [❓](https://github.com/djangocon/2016.djangocon.us/commits?author=kojoidrissa)
[![Timothy Allen](https://avatars.githubusercontent.com/u/68164?v=3&s=100)<br />Timothy Allen](https://github.com/FlipperPA) | [❓](https://github.com/djangocon/2016.djangocon.us/commits?author=FlipperPA)
[![Kenneth Love](https://avatars.githubusercontent.com/u/11908?v=3&s=100)<br />Kenneth Love](https://github.com/kennethlove) | [❓](https://github.com/djangocon/2016.djangocon.us/commits?author=kennethlove)
[![Baptiste Mispelon](https://avatars.githubusercontent.com/u/6345?v=3&s=100)<br />Baptiste Mispelon](https://github.com/bmispelon) | [💻❓](https://github.com/djangocon/2016.djangocon.us/commits?author=bmispelon)
[![Shawn Inman](https://avatars.githubusercontent.com/u/216237?v=3&s=100)<br />Shawn Inman](https://github.com/shawninman) | [💻❓](https://github.com/djangocon/2016.djangocon.us/commits?author=shawninman)
[![Clay Wells](https://avatars.githubusercontent.com/u/812026?v=3&s=100)<br />Clay Wells](https://github.com/clayball) | [❓](https://github.com/djangocon/2016.djangocon.us/commits?author=clayball)

#### Emoji key

Emoji | Represents | Links to
:---: | --- | ---
💻 | Code | `https://github.com/${ownerName}/${repoName}/commits?author=${username}`
📖 | Documentation | `https://github.com/${ownerName}/${repoName}/commits?author=${username}`, Wiki, or other source of documentation
❓ | Answering Questions (in Issues, Stack Overflow, Gitter, Slack, etc.)
🎨 | Design | the logo/iconography/visual design/etc.
👀 | Reviewed Pull Requests


License
---------------

[BSD License](LICENSE)
