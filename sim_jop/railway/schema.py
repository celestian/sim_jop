#!/usr/bin/env python3

import yaml

from sim_jop.railway.elements import Area, Meta, District, Entrypoint, Junction, Signal, Track


class Schema(yaml.YAMLObject):

    yaml_tag = u'!Schema'
    yaml_flow_style = False

    def __init__(self, area, meta, elements):

        keys = list(elements.keys())

        self.area = area
        self.meta = meta
        self.districts = [elements[key] for key in keys if isinstance(elements[key], District)]
        self.entrypoints = [elements[key] for key in keys if isinstance(elements[key], Entrypoint)]
        self.junctions = [elements[key] for key in keys if isinstance(elements[key], Junction)]
        self.signals = [elements[key] for key in keys if isinstance(elements[key], Signal)]
        self.tracks = [elements[key] for key in keys if isinstance(elements[key], Track)]

        self.distances = self._get_distances()

    def _get_distances(self):

        distances = []
        for element in self.junctions:
            if element.distance not in distances:
                distances.append(element.distance)
        for element in self.signals:
            if element.distance not in distances:
                distances.append(element.distance)
        for element in self.tracks:
            if element.start not in distances:
                distances.append(element.start)
            if element.end not in distances:
                distances.append(element.end)

        return sorted(distances)

    def _go_through(self, previous_element, element, level):

        coordinates = {}

        if isinstance(element, Signal):
            coordinates[element.name] = {'row': level,
                                         'column': self.distances.index(element.distance)
                                         }
            next_element = element.facing if previous_element is not element.facing else element.trailing
            coordinates.update(self._go_through(element, next_element, level))

        if isinstance(element, Track):
            mark = 'start' if previous_element == element.start_connection else 'end'
            name = '{}_{}'.format(element.name, mark)
            coordinates[name] = {'row': level, 'column': self.distances.index(
                element.start if previous_element == element.start_connection else element.end)}

        return coordinates

    def get_coordinates(self):

        coordinates = {}

        for element in self.junctions:

            coordinates[element.name] = {'row': element.level,
                                         'column': self.distances.index(element.distance),
                                         }

            if element.kind == 1 or element.kind == 4:
                coordinates.update(self._go_through(element, element.facing, element.level))
                coordinates.update(self._go_through(element, element.trailing, element.level))
                coordinates.update(self._go_through(element, element.sidding, element.level + 1))
                continue

            if element.kind == 2 or element.kind == 3:
                coordinates.update(self._go_through(element, element.facing, element.level - 1))
                coordinates.update(self._go_through(element, element.trailing, element.level + 1))
                coordinates.update(self._go_through(element, element.sidding, element.level))
                continue

            if element.kind == 5 or element.kind == 8:
                coordinates.update(self._go_through(element, element.facing, element.level))
                coordinates.update(self._go_through(element, element.trailing, element.level))
                coordinates.update(self._go_through(element, element.sidding, element.level - 1))
                continue

            if element.kind == 6 or element.kind == 7:
                coordinates.update(self._go_through(element, element.facing, element.level + 1))
                coordinates.update(self._go_through(element, element.trailing, element.level - 1))
                coordinates.update(self._go_through(element, element.sidding, element.level))
                continue

        return coordinates


def create_schema(source_file):

    area = None
    meta = None
    elements = {}

    with open(source_file, 'r') as source:
        data = yaml.safe_load(source)

    if 'area' in data:
        area = Area(data['area'])

    if 'meta' in data:
        meta = Meta(data['meta'])

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
        if isinstance(element, Track):
            if element.start_connection not in keys:
                print('ERROR: {} missing start_connection element {}.'.format(
                    element.name, element.start_connection))
                exit(0)
            if element.end_connection not in keys:
                print('ERROR: {} missing end_connection element {}.'.format(
                    element.name, element.end_connection))
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
        if isinstance(element, Track):
            element.start_connection = elements[element.start_connection]
            element.end_connection = elements[element.end_connection]

    return Schema(area, meta, elements)
