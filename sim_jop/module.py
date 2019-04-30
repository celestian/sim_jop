#!/usr/bin/env python3

import pyglet

from sim_jop.railway.schema import Schema
from sim_jop.gui.chart import Chart
from sim_jop.gui.layout import Layout
from sim_jop.gui.window import EditorWindow


def start_application(args):

    schema = Schema(args['<area.yaml>'])
    chart = Chart(schema)

    layout = Layout()
    layout.add(chart)

    EditorWindow(800, 600, 1, layout)
    pyglet.app.run()
