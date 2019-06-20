#!/usr/bin/env python3

"""opnl2json
Usage:
  opnl2json <raw_github_file>
  opnl2json (-h | --help)
  opnl2json --version
Options:
 -h --help     Show this screen.
 --version     Show version.
"""

from docopt import docopt
import tempfile
import logging
import configparser
import requests


LOG = logging.getLogger(__name__)

def main():
    """
    Entry point
    """

    args = docopt(__doc__, version='opnl2json 0.0.1')
    logging.basicConfig(level=logging.INFO)

    response = requests.get(args['<raw_github_file>'])

    if 200 == response.status_code:
        parser = configparser.ConfigParser(allow_no_value=True)
        parser.read_string(response.text[1:])
        LOG.info(parser.sections())

if __name__ == '__main__':
    main()
