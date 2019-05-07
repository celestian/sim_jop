#!/usr/bin/env python3

import logging
import pyglet

from sim_jop.railway.schema import Schema
from sim_jop.gui.chart import Chart
from sim_jop.gui.layout import Layout
from sim_jop.gui.window import EditorWindow


LOG = logging.getLogger(__name__)


def start_editor(args):

    window = EditorWindow()
    window.set_visible()
    window.on_draw()

    pyglet.app.run()
