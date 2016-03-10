#!/usr/bin/env python
from __future__ import print_function
import sys
import subprocess
import re
import datetime

def notify(text, title="Error"):
    script = 'display notification "{}" with title "Error" subtitle "world" sound name "Funk"'.format(text)
    subprocess.Popen(['osascript', '-e', script])


def watch_for_error(proc):
    regex = re.compile(r'^\s+"formatted"\: "Error: (.*)",$',
                       re.UNICODE | re.DOTALL | re.MULTILINE)
    for line in iter(proc.stderr.readline, b''):
        print(datetime.datetime.now())
        print(line, file=sys.stderr, end="")
        try:
            error = regex.match(line).groups()[0]
            notify(error)
        except AttributeError:
            pass


def main():
    cmd = sys.argv[1:]
    proc = subprocess.Popen(cmd, stderr=subprocess.PIPE)
    try:
        watch_for_error(proc)
    except KeyboardInterrupt:
        proc.kill()
        exit()

if __name__ == '__main__':
    main()