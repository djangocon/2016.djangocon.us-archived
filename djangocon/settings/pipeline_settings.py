PIPELINE_CSS = {
    'base': {
        'source_filenames': (
          'css/bootstrap.min.css',
          'fonts/stylesheet.css',
          'css/main.css'
        ),
        'output_filename': 'main.css',
        'extra_context': {
            'media': 'screen,projection',
        },
    },
}

PIPELINE_JS = {
    'base': {
        'source_filenames': (
          'js/vendor/jquery-1.11.2.min.js',
          'js/vendor/bootstrap.min.js',
        ),
        'output_filename': 'main.js',
    }
}

