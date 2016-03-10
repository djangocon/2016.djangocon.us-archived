SHELL=/bin/bash -eu -o pipefail
NPM_BIN := $(shell pwd)/node_modules/.bin

# --- Utils --------------------------------------------------------------------

# Copy all assets from client > build. Just symlink them.
# No processing necessary
assets:
	mkdir -p build && rm -f build/assets && ln -s ../client/assets build/assets

clean:
	rm -rf build/*

collect:
	$(shell pwd)/manage.py collectstatic --noinput

# --- CSS ----------------------------------------------------------------------

# Standard CSS compilation. Compile SCSS to CSS and run it
# through autoprefixer.
buildcss = cat $(1) \
	| $(NPM_BIN)/node-sass --include-path client/scss --output-style compressed \
	| $(NPM_BIN)/postcss --use autoprefixer --autoprefixer.browsers "last 2 versions" \
 	> $(2)

ifdef watch
	# Watch for css changes. This works 'on folders' and not specific files
	# and also doesn't run autoprefixer.
	#buildcss = $(NPM_BIN)/node-sass client/scss -o build/css --source-map=true --watch | grep -e '"formatted": "Error' > notify.sh
	buildcss = $(NPM_BIN)/node-sass client/scss -o build/css --source-map=true --watch
	#buildcss = $(NPM_BIN)/node-sass client/scss -o build/css --source-map=true --watch 2> >(grep '' 1>&2) > log.txt

endif

css:
	mkdir -p build/css && \
	$(call buildcss, client/scss/base.scss, build/css/base.css)

# --- JS -----------------------------------------------------------------------

# Standard JS build process, collect all JS files with browserify
# and compress them with uglifyjs.
buildjs = $(NPM_BIN)/browserify -t babelify --presets es2015 $(1) \
	| $(NPM_BIN)/uglifyjs --mangle --compress warnings=false \
	> $(2)

ifdef watch
	# Watch for changes, and no autoprefixer since it doesn't work
	# well together.
	buildjs = $(NPM_BIN)/watchify -t babelify --presets es2015 $(1) -o $(2) --verbose --debug
endif

js:
	mkdir -p build/js && \
	$(call buildjs, client/js/base.js, build/js/base.js)

# ------------------------------------------------------------------------------

all: assets css js

.PHONY: clean assets css js collect
