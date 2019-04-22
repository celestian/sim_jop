#!/usr/bin/env python3

import pyglet


class Grid:

    def __init__(self):

        width = 800
        heigth = 600

        points = []

        for w in range(0, width, 8):
            for h in range(0, heigth, 12):
                points.append(w)
                points.append(h)

        number = int(len(points) / 2.0)
        self.vertices = pyglet.graphics.vertex_list(number,
                                                    ('v2i', points),
                                                    ('c3B', [255, 0, 0] * number)
                                                    )

        print(number)


class EditorWindow(pyglet.window.Window):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.grid = Grid()

    def on_draw(self):
        self.clear()
        self.grid.vertices.draw(pyglet.gl.GL_POINTS)
