#!/usr/bin/env python
import os
import sys


if __name__ == "__main__":
    settings = 'local'

    if 'test' in sys.argv:
        # Running tests - use test-specific settings
        settings = "test"

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangocon.settings.%s" % settings)

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
