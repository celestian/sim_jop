#!/usr/bin/env python3


class View:

    def __init__(self, width, height, zoom_level):
        coefficient = (zoom_level + 1) * 2

        self.width = width
        self.height = height

        self.box_width = 2 * coefficient
        self.box_height = 3 * coefficient

    def get_width(self, plan_width):
        plan_width = plan_width + 10
        return plan_width * self.box_width

    def get_height(self, plan_height):
        plan_height = plan_height + 10
        return plan_height * self.box_height
