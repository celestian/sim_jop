#!/usr/bin/env python3

import yaml


area_structure = [
    {
        'label': 'area_id',
        'type': int,
    }, {
        'label': 'name',
        'type': str,
    },
]

meta_structure = [
    {
        'label': 'author',
        'type': str,
    }, {
        'label': 'email',
        'type': str,
    }, {
        'label': 'date',
        'type': str,
    }, {
        'label': 'version',
        'type': int,
    },
]

district_structure = [
    {
        'label': 'name',
        'type': str,
    },
]

entrypoint_structure = [
    {
        'label': 'name',
        'type': str,
    }, {
        'label': 'district',
        'type': str,
    }, {
        'label': 'connection',
        'type': str,
    }, {
        'label': 'direction_type',
        'type': str,
    },
]

junction_structure = [
    {
        'label': 'name',
        'type': str,
    }, {
        'label': 'distance',
        'type': int,
    }, {
        'label': 'district',
        'type': str,
    }, {
        'label': 'type',
        'type': int,
    }, {
        'label': 'level',
        'type': int,
    }, {
        'label': 'facing',
        'type': str,
    }, {
        'label': 'trailing',
        'type': str,
    }, {
        'label': 'sidding',
        'type': str,
    },
]

signal_structure = [
    {
        'label': 'name',
        'type': str,
    }, {
        'label': 'distance',
        'type': int,
    }, {
        'label': 'district',
        'type': str,
    }, {
        'label': 'type',
        'type': str,
    }, {
        'label': 'facing',
        'type': str,
    }, {
        'label': 'trailing',
        'type': str,
    },
]

track_structure = [
    {
        'label': 'name',
        'type': str,
    }, {
        'label': 'start',
        'type': int,
    }, {
        'label': 'end',
        'type': int,
    }, {
        'label': 'type',
        'type': str,
    }, {
        'label': 'start_connection',
        'type': str,
    }, {
        'label': 'end_connection',
        'type': str,
    },
]


def prepare_template(structure, is_array):

    result = ''

    if is_array:
        first_prefix = '- '
    else:
        first_prefix = '  '

    is_first = True
    for item in structure:
        if is_first:
            prefix = first_prefix
            is_first = False
        else:
            prefix = '  '

        if item['type'] is int:
            result = result + prefix + item['label'] + ': 0\n'
        if item['type'] is str:
            result = result + prefix + item['label'] + ': ""\n'

    return result


class Area(yaml.YAMLObject):

    yaml_tag = u'!Area'
    yaml_flow_style = False

    def __init__(self, data):
        self.area_id = int(data['area_id'])
        self.name = data['name']

    @staticmethod
    def get_template(is_array):
        return prepare_template(area_structure, is_array)


class Meta(yaml.YAMLObject):

    yaml_tag = u'!Meta'
    yaml_flow_style = False

    def __init__(self, data):
        self.author = data['author']
        self.email = data['email']
        self.date = data['date']
        self.version = data['version']

    @staticmethod
    def get_template(is_array):
        return prepare_template(meta_structure, is_array)


class District(yaml.YAMLObject):

    yaml_tag = u'!District'
    yaml_flow_style = False

    def __init__(self, data):
        self.name = data['name']

    @staticmethod
    def get_template(is_array):
        return prepare_template(district_structure, is_array)


class Entrypoint(yaml.YAMLObject):

    yaml_tag = u'!Entrypoint'
    yaml_flow_style = False

    def __init__(self, data):
        self.name = data['name']
        self.district = data['district']
        self.connection = data['connection']
        self.direction_type = data['direction_type']

        if self.direction_type not in ('in', 'out', 'both'):
            print('ERROR: entrypoint "{}": incorrect value of direction_type'.format(self.name))
            exit(0)

    @staticmethod
    def get_template(is_array):
        return prepare_template(entrypoint_structure, is_array)


class Junction(yaml.YAMLObject):

    yaml_tag = u'!Junction'
    yaml_flow_style = False

    def __init__(self, data):
        self.name = data['name']
        self.distance = data['distance']
        self.district = data['district']
        self.type = data['type']
        self.level = data['level']
        self.facing = data['facing']
        self.trailing = data['trailing']
        self.sidding = data['sidding']

        if self.type < 1 and self.type > 8:
            print('ERROR: junction "{}": incorrect value of type'.format(self.name))
            exit(0)

    @staticmethod
    def get_template(is_array):
        return prepare_template(junction_structure, is_array)


class Signal(yaml.YAMLObject):

    yaml_tag = u'!Signal'
    yaml_flow_style = False

    def __init__(self, data):
        self.name = data['name']
        self.distance = data['distance']
        self.district = data['district']
        self.type = data['type']
        self.facing = data['facing']
        self.trailing = data['trailing']

        # TODO: check type

    @staticmethod
    def get_template(is_array):
        return prepare_template(signal_structure, is_array)


class Track(yaml.YAMLObject):

    yaml_tag = u'!Track'
    yaml_flow_style = False

    def __init__(self, data):
        self.name = data['name']
        self.start = data['start']
        self.end = data['end']
        self.type = data['type']
        self.start_connection = data['start_connection']
        self.end_connection = data['end_connection']

        # TODO: Check type

    @staticmethod
    def get_template(is_array):
        return prepare_template(track_structure, is_array)
