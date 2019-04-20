#!/usr/bin/env python3

import yaml

from sim_doz.railway.elements import Area, Meta, District, Entrypoint, Junction, Signal, Track


class Schema(yaml.YAMLObject):

    yaml_tag = u'!Schema'
    yaml_flow_style = False

    def __init__(self, area, meta, elements):

        keys = list(elements.keys())

        self.area = area
        self.meta = meta
        self.districts = [elements[key] for key in keys if isinstance(elements[key], District)]
        self.entrypoints = [elements[key] for key in keys if isinstance(elements[key], Entrypoint)]
        self.junctions = [elements[key] for key in keys if isinstance(elements[key], Junction)]
        self.signals = [elements[key] for key in keys if isinstance(elements[key], Signal)]
        self.tracks = [elements[key] for key in keys if isinstance(elements[key], Track)]

    def get_size(self):
        min_distance = self.junctions[0].distance
        max_distance = self.junctions[0].distance

        for e in self.junctions:
            min_distance = e.distance if e.distance < min_distance else min_distance
            max_distance = e.distance if e.distance > max_distance else max_distance

        for e in self.signals:
            min_distance = e.distance if e.distance < min_distance else min_distance
            max_distance = e.distance if e.distance > max_distance else max_distance

        return (min_distance, max_distance)
