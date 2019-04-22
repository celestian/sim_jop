#!/usr/bin/env python3

import pyglet


class Zoom:

    def __init__(self, zoom_level):
        coefficient = (zoom_level + 1) * 2
        self.box_width = 2 * coefficient
        self.box_heigth = 3 * coefficient


class Grid:

    def __init__(self, zoom):

        width = 800
        heigth = 600

        points = []

        for w in range(0, width, zoom.box_width):
            for h in range(0, heigth, zoom.box_heigth):
                points.append(w)
                points.append(h)

        number = int(len(points) / 2.0)
        color = [255, 0, 0]
        self.vertices = pyglet.graphics.vertex_list(
            number, ('v2i', points), ('c3B', color * number))


class EditorWindow(pyglet.window.Window):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.grid = Grid(Zoom(2))

    def on_draw(self):
        self.clear()
        self.grid.vertices.draw(pyglet.gl.GL_POINTS)
