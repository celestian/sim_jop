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
import json


LOG = logging.getLogger(__name__)

def main():
    """
    Entry point
    """

    args = docopt(__doc__, version='opnl2json 0.0.1')
    logging.basicConfig(level=logging.INFO)

    result = {'track': [], 'signal': []}
    result_key = 0

    response = requests.get(args['<raw_github_file>'])

    if 200 == response.status_code:
        parser = configparser.ConfigParser(allow_no_value=True)
        parser.read_string(response.text[1:])

        if 'G' not in parser.sections():
            print("Wrong format.")

        print(parser.sections())

        if 'ver' in parser['G']:
            version = parser['G']['ver']
            if version not in ['1.1']:
                print("Unsuported format.")
            print("version: {}".format(version))

        if 'P' in parser.sections():
            signal_count = int(parser['P']['N'])
            track_count = int(parser['P']['U'])

        for i in range(track_count):
            key = 'U{}'.format(i)
            #         "track": [{"key": 0, "x":3, "y": 3, "len": 3}],

            sections = parser[key]['S']
            chunks = [sections[i:i + 8] for i in range(0, len(sections), 8)]
            for chunk in chunks:
                x = chunk[0:3]
                y = chunk[3:6]
                t = int(chunk[6:8])
                # 12 je asi rovne => type = 1
                # 14 je asi sikmo -> type = 2
                type = 1
                if t == 14:
                    type = 2
                    print("type 2", result_key)
                result['track'].append({'key': result_key, 'x': x, 'y': y, 'len': 1, 'type': type})
                result_key = result_key + 1

        for i in range(signal_count):
            key = 'N{}'.format(i)
            symbol = int(parser[key]['S'])
            if symbol == 0:
                dir = 'r'
                type = 1
            if symbol == 1:
                dir = 'l'
                type = 1
            if symbol == 4:
                dir = 'r'
                type = 2
            if symbol == 5:
                dir = 'l'
                type = 2
            result['signal'].append({'key': result_key, 'x':int(parser[key]['X']), 'y': int(parser[key]['Y']), 'type': type, 'dir': dir, 'signal': 'green'})
            result_key = result_key + 1

        print(json.dumps(result, sort_keys=True))

if __name__ == '__main__':
    main()
