#!/usr/bin/env python3

class Layout:

    def __init__(self):
        self._charts = []

    def add(self, chart):
        self._charts.append(chart)

    def draw(self):

        for chart in self._charts:
            chart.draw()
