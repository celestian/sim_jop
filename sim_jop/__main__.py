#!/usr/bin/env python3

"""sim_jop
Usage:
  sim_jop editor <schema.yaml>
  sim_jop (-h | --help)
  sim_jop --version
Options:
 -h --help     Show this screen.
 --version     Show version.
"""

from docopt import docopt
import logging

from sim_jop.module import start_editor


def main():
    """
    Entry point
    """

    args = docopt(__doc__, version='sim_jop 0.0.2')

    logging.basicConfig(level=logging.INFO)

    if args['editor'] and args['<schema.yaml>']:
        start_editor(args)


if __name__ == '__main__':
    main()
