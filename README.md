DjangoCon US 2016
=================

DjangoCon US 2016 is built on top of [Pinax Symposion](https://github.com/pinax/symposion) and [PinaxCon](https://github.com/pinax/PinaxCon). With our changes, your mileage may vary.


Code of Conduct
---------------

As a contributor, you can help us keep the Django community open and inclusive.
Please read and follow our `Code of Conduct <https://www.djangoproject.com/conduct/>`_.


Getting Started
----------------

Make sure you are using a virtual environment of some sort (e.g. `virtualenv` or
`pyenv`).

    $ createdb djangocon2016

    $ pip install -r requirements.txt

    $ ./manage.py migrate

    $ ./manage.py loaddata fixtures/*

    $ ./manage.py createsuperuser

    $ ./manage.py runserver


Static files
------------

The static file compilation is done with Node dependencies. On a Mac install
node via Homebrew:

    $ brew install node

Ideally, create a virtualenv and activate it

Install all node dev dependencies:

    $ npm install

Install requirements:

    $ pip install -r requirements.txt

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
