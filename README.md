The static file compilation is done with Node dependencies. On a Mac install
node via Homebrew:

    $ brew install node

Install all node dev dependencies:

    $ npm install

To compile all static files simply run:

    $ make all

Finally collect those static files and start the development server:

    $ manage.py collectstatic
    $ manage.py runserver

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
