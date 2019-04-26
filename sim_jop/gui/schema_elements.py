#!/usr/bin/env python3

import pyglet


class GTrack:

    def __init__(self, plan_width, plan_heigth, zoom):

        x = zoom.get_width(plan_width)
        y = zoom.get_heigth(plan_heigth) + int((zoom.box_heigth - 2) / 2.0)
        dest_x = zoom.get_width(plan_width) + zoom.box_width
        dest_y = zoom.get_heigth(plan_heigth) + int((zoom.box_heigth - 2) / 2.0)

        color = [255, 0, 0]
        self.vertices = pyglet.graphics.vertex_list(
            2, ('v2i', (x, y, dest_x, dest_y)), ('c3B', color * 2))
