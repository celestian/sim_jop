#!/usr/bin/env python3

"""sim_doz
Usage:
  sim_doz schema prepare <area.yaml>
  sim_doz schema create <area.yaml>
  sim_doz editor
  sim_doz (-h | --help)
  sim_doz --version
Options:
 -h --help     Show this screen.
 --version     Show version.
"""

from docopt import docopt
import yaml
import pyglet

from sim_doz.schema import prepare_schema, create_schema
from sim_doz.module import EditorWindow


def main():
    """
    Entry point
    """

    args = docopt(__doc__, version='sim_doz 0.0.1')

    if args['schema'] and args['prepare']:
        prepare_schema(args['<area.yaml>'])

    if args['schema'] and args['create']:
        create_schema(args['<area.yaml>'])

    if args['editor']:
        EditorWindow(800, 600, 'sim_doz')
        pyglet.app.run()


if __name__ == '__main__':
    main()
