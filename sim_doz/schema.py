#!/usr/bin/env python3

import yaml
import json

from sim_doz.railway.elements import Area, Meta, District, Entrypoint, Junction, Signal, Track


def prepare_schema(output_file):

    district_number = int(input('Počet železničních obvodů (district): '))
    entrypoint_number = int(input('Počet vstupních uzlů (entrypoint): '))
    junction_number = int(input('Počet výhybek (junction): '))
    signal_number = int(input('Počet návěstidel (signal): '))
    track_number = int(input('Počet kolejí (track): '))

    with open(output_file, 'w') as outfile:
        outfile.write('area:\n')
        outfile.write(Area.get_template(is_array=False))

        outfile.write('meta:\n')
        outfile.write(Meta.get_template(is_array=False))

        outfile.write('district:\n')
        for _ in range(district_number):
            outfile.write(District.get_template(is_array=True))

        outfile.write('entrypoint:\n')
        for _ in range(entrypoint_number):
            outfile.write(Entrypoint.get_template(is_array=True))

        outfile.write('junction:\n')
        for _ in range(junction_number):
            outfile.write(Junction.get_template(is_array=True))

        outfile.write('signal:\n')
        for _ in range(signal_number):
            outfile.write(Signal.get_template(is_array=True))

        outfile.write('track:\n')
        for _ in range(track_number):
            outfile.write(Track.get_template(is_array=True))


def create_schema(source_file):

    elements = {}

    with open(source_file, 'r') as source:
        data = yaml.safe_load(source)

    if 'area' in data:
        if 'name' in data['area']:
            elements[data['area']['name']] = Area(data['area'])

    # TODO: load also meta data

    if 'district' in data:
        for item in data['district']:
            elements[item['name']] = District(item)

    if 'entrypoint' in data:
        for item in data['entrypoint']:
            elements[item['name']] = Entrypoint(item)

    if 'junction' in data:
        for item in data['junction']:
            elements[item['name']] = Junction(item)

    if 'signal' in data:
        for item in data['signal']:
            elements[item['name']] = Signal(item)

    if 'track' in data:
        for item in data['track']:
            elements[item['name']] = Track(item)

    # integrity check
    keys = list(elements.keys())
    for key in keys:
        element = elements[key]
        if isinstance(element, Entrypoint):
            if element.connection not in keys:
                print('ERROR: {} missing connection element {}.'.format(
                    element.name, element.connection))
                exit(0)
        if isinstance(element, (Entrypoint, Junction, Signal)):
            if element.district not in keys:
                print('ERROR: {} missing district element {}.'.format(
                    element.name, element.district))
                exit(0)
        if isinstance(element, (Junction, Signal)):
            if element.facing not in keys:
                print('ERROR: {} missing facing element {}.'.format(
                    element.name, element.facing))
                exit(0)
            if element.trailing not in keys:
                print('ERROR: {} missing trailing element {}.'.format(
                    element.name, element.trailing))
                exit(0)
        if isinstance(element, Junction):
            if element.sidding not in keys:
                print('ERROR: {} missing sidding element {}.'.format(
                    element.name, element.sidding))
                exit(0)

    # create connections
    for key in keys:
        element = elements[key]
        if isinstance(element, Entrypoint):
            element.connection = elements[element.connection]
        if isinstance(element, (Entrypoint, Junction, Signal)):
            element.district = elements[element.district]
        if isinstance(element, (Junction, Signal)):
            element.facing = elements[element.facing]
            element.trailing = elements[element.trailing]
        if isinstance(element, Junction):
            element.sidding = elements[element.sidding]
