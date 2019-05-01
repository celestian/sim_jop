#!/usr/bin/env python3


class ChartElement:

    def __init__(self, element, coord_x, coord_y):

        self.element = element
        self.name = element.name
        self.type = self._get_type()
        self.coord_x = coord_x
        self.coord_y = coord_y

    def _get_type(self):

        element_type = None

        if isinstance(element, Junction):
            element_type = 'junction'
        if isinstance(element, Signal):
            element_type = 'signal'
        if isinstance(element, Track):
            element_type = 'track'

        return element_type

class Chart:

    def __init__(self, schema):

        self._schema = schema

    def _build_schema(self):
        pass

    def _go_through(self, previous_element, element, level):

        coordinates = {}

        distances = self._schema.get_distances()

        if isinstance(element, Signal):
            coordinates[element.name] = {'row': level,
                                         'column': distances.index(element.distance)
                                         }
            next_element = element.facing if previous_element is not element.facing else element.trailing
            coordinates.update(self._go_through(element, next_element, level))

        if isinstance(element, Track):
            mark = 'start' if previous_element == element.start_connection else 'end'
            name = '{}_{}'.format(element.name, mark)
            coordinates[name] = {'row': level, 'column': distances.index(
                element.start if previous_element == element.start_connection else element.end)}

        return coordinates

    def get_coordinates(self):

        coordinates = {}

        distances = self._schema.get_distances()

        for element in self.junctions:

            coordinates[element.name] = {'row': element.level,
                                         'column': distances.index(element.distance),
                                         }

            if element.type == 1 or element.type == 4:
                coordinates.update(self._go_through(element, element.facing, element.level))
                coordinates.update(self._go_through(element, element.trailing, element.level))
                coordinates.update(self._go_through(element, element.sidding, element.level + 1))
                continue

            if element.type == 2 or element.type == 3:
                coordinates.update(self._go_through(element, element.facing, element.level - 1))
                coordinates.update(self._go_through(element, element.trailing, element.level + 1))
                coordinates.update(self._go_through(element, element.sidding, element.level))
                continue

            if element.type == 5 or element.type == 8:
                coordinates.update(self._go_through(element, element.facing, element.level))
                coordinates.update(self._go_through(element, element.trailing, element.level))
                coordinates.update(self._go_through(element, element.sidding, element.level - 1))
                continue

            if element.type == 6 or element.type == 7:
                coordinates.update(self._go_through(element, element.facing, element.level + 1))
                coordinates.update(self._go_through(element, element.trailing, element.level - 1))
                coordinates.update(self._go_through(element, element.sidding, element.level))
                continue

        return coordinates

    def draw(self, view):
        pass
        # line = GTrack(self.area[e]['column'], self.area[e]['row'], self._zoom)
        # e.vertices.draw(pyglet.gl.GL_LINES)
