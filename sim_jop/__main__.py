#!/usr/bin/env python3

"""sim_jop
Usage:
  sim_jop schema prepare <area.yaml>
  sim_jop schema check <area.yaml>
  sim_jop schema show <area.yaml>
  sim_jop (-h | --help)
  sim_jop --version
Options:
 -h --help     Show this screen.
 --version     Show version.
"""

from docopt import docopt
import yaml
import pyglet

from sim_jop.schema import prepare_schema, create_schema
from sim_jop.module import EditorWindow


def main():
    """
    Entry point
    """

    args = docopt(__doc__, version='sim_jop 0.0.1')

    if args['schema'] and args['prepare']:
        prepare_schema(args['<area.yaml>'])

    if args['schema'] and args['check']:
        create_schema(args['<area.yaml>'])

    if args['schema'] and args['show']:
        EditorWindow(800, 600, create_schema(args['<area.yaml>']))
        pyglet.app.run()


if __name__ == '__main__':
    main()
