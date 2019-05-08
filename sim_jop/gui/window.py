#!/usr/bin/env python3

import logging
import pyglet

from sim_jop.gui.view import View
from sim_jop.gui.schema_elements import GTrack

# Coordinate system:
# * window: width, height
# * plan: plan_width, plan_height
# * box: box_width, box_height

LOG = logging.getLogger(__name__)


class Menu:

    def __init__(self, position):
        self.position = position
        self.batch = pyglet.graphics.Batch()

        points = []
        points.extend([self.position['width_start'], self.position['height_start']])
        points.extend([self.position['width_end'], self.position['height_start']])
        points.extend([self.position['width_end'], self.position['height_end']])
        points.extend([self.position['width_start'], self.position['height_end']])
        points.extend([self.position['width_start'], self.position['height_start'] - 1])

        color = [0, 180, 190]
        self.palette = pyglet.graphics.vertex_list_indexed(
            5, [0, 1, 1, 2, 2, 3, 3, 4], ('v2i', points), ('c3B', color * 5))

    def draw(self):
        self.palette.draw(pyglet.gl.GL_LINES)


class Grid:

    def __init__(self, width, height, box_width, box_height):

        self.batch = pyglet.graphics.Batch()

        points = []
        self.labels = []

        for w in range(0, width, box_width * 5):
            for h in range(0, height, box_height * 5):
                if w == 0:
                    label = pyglet.text.Label('{:d}'.format(
                        int(h / box_height)), font_name='Ariel', font_size=10, x=w, y=h, color=(0, 180, 190, 200))
                    self.labels.append(label)
                    points.extend([0, h, width, h])
                if h == 0:
                    label = pyglet.text.Label('{:d}'.format(
                        int(w / box_width)), font_name='Ariel', font_size=10, x=w, y=h, color=(0, 180, 190, 200))
                    self.labels.append(label)
                    points.extend([w, 0, w, height])

        number = int(len(points) / 2.0)
        color = [30, 30, 40]
        self.batch.add(number, pyglet.gl.GL_LINES, None, ('v2i', points), ('c3B', color * number))

    def draw(self):
        self.batch.draw()
        for label in self.labels:
            label.draw()


class EditorWindow(pyglet.window.Window):

    def __init__(self):
        super().__init__(fullscreen=True, visible=False, caption='sim_jop')
        self.set_mouse_visible(False)
        LOG.info('Resolution: {}x{}'.format(self.width, self.height))

        self.zoom_level = 1
        self.pos_x, self.pos_y = (0, 0)
        self.cursor = None

        coefficient = (self.zoom_level + 1) * 2
        self.box_width = 2 * coefficient
        self.box_height = 3 * coefficient
        self.max_x = int(self.width / self.box_width)
        self.max_y = int(self.height / self.box_height)

        menu_position = {
            'width_start': 1,
            'width_end': self.width,
            'height_start': self.height - (15 * self.box_height) + 1,
            'height_end': self.height,
        }
        grid_position = {
            'width_start': 1,
            'width_end': self.width,
            'height_start': 0,
            'height_end': self.height - (15 * self.box_height) - 1,
        }

        self.menu = Menu(menu_position)

        self.grid = Grid(
            self.width,
            self.height -
            15 *
            self.box_height,
            self.box_width,
            self.box_height)
        self._set_cursor()

        self.is_grid_on = False

    def _get_box(self, pos_x, pos_y):
        box_x = int(pos_x / self.box_width) if pos_x / self.box_width < self.max_x else self.max_x
        box_y = int(pos_y / self.box_height) if pos_y / \
            self.box_height < self.max_y - 1 else self.max_y - 1
        return (box_x, box_y)

    def _set_cursor(self):

        points = []
        points.extend([self.pos_x * self.box_width, self.pos_y * self.box_height])
        points.extend([(self.pos_x + 1) * self.box_width, self.pos_y * self.box_height])
        points.extend([(self.pos_x + 1) * self.box_width, (self.pos_y + 1) * self.box_height])
        points.extend([self.pos_x * self.box_width, (self.pos_y + 1) * self.box_height])
        points.extend([self.pos_x * self.box_width, self.pos_y * self.box_height - 1])

        color = [255, 0, 0]
        self.cursor = pyglet.graphics.vertex_list_indexed(
            5, [0, 1, 1, 2, 2, 3, 3, 4], ('v2i', points), ('c3B', color * 5))

    def on_mouse_motion(self, x, y, dx, dy):

        self.pos_x, self.pos_y = self._get_box(x, y)
        self._set_cursor()
        self.on_draw()

    def on_key_press(self, symbol, modifiers):
        if symbol == pyglet.window.key.Q:
            pyglet.app.exit()
        if symbol == pyglet.window.key.G:
            self.is_grid_on = False if self.is_grid_on else True

    def on_draw(self):
        self.clear()
        self.menu.draw()
        if self.is_grid_on:
            self.grid.draw()
        self.cursor.draw(pyglet.gl.GL_LINES)
