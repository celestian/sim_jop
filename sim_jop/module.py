#!/usr/bin/env python3

import pyglet

from sim_jop.railway.schema import create_schema
from sim_jop.gui.window import EditorWindow


def start_application(args):
    EditorWindow(800, 600, create_schema(args['<area.yaml>']))
    pyglet.app.run()
