#!/usr/bin/env python3

import pyglet

from sim_jop.gui.view import View
from sim_jop.gui.schema_elements import GTrack

# Coordinate system:
# * window: width, height
# * plan: plan_width, plan_height
# * box: box_width, box_height


class Grid:

    def __init__(self, view):

        self._view = view

        points = []

        for w in range(0, self._view.width, self._view.box_width):
            for h in range(0, self._view.height, self._view.box_height):
                points.append(w)
                points.append(h)

        number = int(len(points) / 2.0)
        color = [255, 0, 0]
        self.vertices = pyglet.graphics.vertex_list(
            number, ('v2i', points), ('c3B', color * number))

    def draw(self):
        self.vertices.draw(pyglet.gl.GL_POINTS)


class EditorWindow(pyglet.window.Window):

    def __init__(self, width, height, zoom_level, layout):

        super().__init__(width, height, caption='sim_jop')

        self._width = width
        self._height = height
        self._zoom_level = zoom_level

        self._view = View(self._width, self._height, self._zoom_level)

        self._grid = Grid(self._view)
        self._layout = layout

    def on_draw(self):
        self.clear()
        self._grid.draw()
        self._layout.draw(self._view)
