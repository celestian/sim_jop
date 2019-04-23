#!/usr/bin/env python3

import pyglet

# Coordinate system:
# * window: width, heigth
# * plan: plan_width, plan_heigth
# * box: box_width, box_heigth


class Zoom:

    def __init__(self, zoom_level):
        coefficient = (zoom_level + 1) * 2
        self.box_width = 2 * coefficient
        self.box_heigth = 3 * coefficient

    def get_width(self, plan_width):
        plan_width = plan_width + 10
        return (plan_width * self.box_width)

    def get_heigth(self, plan_heigth):
        plan_heigth = plan_heigth + 10
        return (plan_heigth * self.box_heigth)


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


class GTrack:

    def __init__(self, plan_width, plan_heigth, zoom):

        x = zoom.get_width(plan_width)
        y = zoom.get_heigth(plan_heigth) + int((zoom.box_heigth - 2) / 2.0)
        dest_x = zoom.get_width(plan_width) + zoom.box_width
        dest_y = zoom.get_heigth(plan_heigth) + int((zoom.box_heigth - 2) / 2.0)

        color = [255, 0, 0]
        self.vertices = pyglet.graphics.vertex_list(
            2, ('v2i', (x, y, dest_x, dest_y)), ('c3B', color * 2))


class EditorWindow(pyglet.window.Window):

    def __init__(self, width, heigth, area):
        super().__init__(width, heigth, caption='sim_doz')
        self.zoom = Zoom(1)
        self.grid = Grid(self.zoom)
        self.area = area
        # self.line = GTrack(10, 5, self.zoom)

        self.lines = []
        for e in self.area:
            line = GTrack(self.area[e]['colomn'], self.area[e]['row'], self.zoom)
            self.lines.append(line)

    def on_draw(self):
        self.clear()
        self.grid.vertices.draw(pyglet.gl.GL_POINTS)
        # self.line.vertices.draw(pyglet.gl.GL_LINES)

        for e in self.lines:
            e.vertices.draw(pyglet.gl.GL_LINES)
