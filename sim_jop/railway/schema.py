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
                                         'colomn': self.distances.index(element.distance)
                                         }
            next_element = element.facing if previous_element is not element.facing else element.trailing
            coordinates.update(self._go_through(element, next_element, level))

        if isinstance(element, Track):
            mark = 'start' if previous_element == element.start_connection else 'end'
            name = '{}_{}'.format(element.name, mark)
            coordinates[name] = {'row': level, 'colomn': self.distances.index(
                element.start if previous_element == element.start_connection else element.end)}

        return coordinates

    def get_coordinates(self):

        coordinates = {}

        for element in self.junctions:

            coordinates[element.name] = {'row': element.level,
                                         'colomn': self.distances.index(element.distance),
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
