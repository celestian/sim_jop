#!/usr/bin/env python3

import pyglet


class Rectangle:

    def __init__(self, batch, group, geometry, color):

        self.vertex_list = batch.add_indexed(
            5, pyglet.gl.GL_LINES, group, [
                0, 1, 1, 2, 2, 3, 3, 4], ('v2i', self._points(geometry)), ('c3B', color * 5))

    def __del__(self):
        self.vertex_list.delete()

    def _points(self, geometry):
        points = []
        points.extend([geometry['width_start'], geometry['height_start']])
        points.extend([geometry['width_end'], geometry['height_start']])
        points.extend([geometry['width_end'], geometry['height_end']])
        points.extend([geometry['width_start'], geometry['height_end']])
        points.extend([geometry['width_start'], geometry['height_start'] - 1])
        return points

    def move(self, geometry):
        self.vertex_list.vertices = self._points(geometry)
