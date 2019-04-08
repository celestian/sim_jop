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
        'type': str,
    }, {
        'label': 'orientation',
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
        self._area_id = int(data['area_id'])
        self._name = data['name']

    @staticmethod
    def get_template(is_array):
        return prepare_template(area_structure, is_array)

    @property
    def area_id(self):
        return self._area_id

    @property
    def name(self):
        return self._name


class Meta(yaml.YAMLObject):

    yaml_tag = u'!Meta'
    yaml_flow_style = False

    def __init__(self, author, email, date, version):
        self._author = author
        self._email = email
        self._date = date
        self._version = version

    @staticmethod
    def get_template(is_array):
        return prepare_template(meta_structure, is_array)

    @property
    def author(self):
        return self._author

    @property
    def email(self):
        return self._email

    @property
    def date(self):
        return self._date

    @property
    def version(self):
        return self._version


class District(yaml.YAMLObject):

    yaml_tag = u'!District'
    yaml_flow_style = False

    def __init__(self, data):
        self._name = data['name']

    @staticmethod
    def get_template(is_array):
        return prepare_template(district_structure, is_array)

    @property
    def name(self):
        return self._name


class Entrypoint(yaml.YAMLObject):

    yaml_tag = u'!Entrypoint'
    yaml_flow_style = False

    def __init__(self, data):
        self._name = data['name']
        self._district = data['district']

    @staticmethod
    def get_template(is_array):
        return prepare_template(entrypoint_structure, is_array)

    @property
    def name(self):
        return self._name

    @property
    def district(self):
        return self._district


class Junction(yaml.YAMLObject):

    yaml_tag = u'!Junction'
    yaml_flow_style = False

    def __init__(self, data):
        self._name = data['name']
        self._distance = data['distance']
        self._district = data['district']
        self._type = data['type']
        self._orientation = data['orientation']
        self._facing = data['facing']
        self._trailing = data['trailing']
        self._sidding = data['sidding']

    @staticmethod
    def get_template(is_array):
        return prepare_template(junction_structure, is_array)

    @property
    def name(self):
        return self._name

    @property
    def distance(self):
        return self._distance

    @property
    def district(self):
        return self._district

    @property
    def type(self):
        return self._type

    @property
    def orientation(self):
        return self._orientation

    @property
    def facing(self):
        return self._facing

    @property
    def trailing(self):
        return self._trailing

    @property
    def sidding(self):
        return self._sidding


class Signal(yaml.YAMLObject):

    yaml_tag = u'!Signal'
    yaml_flow_style = False

    def __init__(self, data):
        self._name = data['name']
        self._distance = data['distance']
        self._district = data['district']
        self._type = data['type']
        self._facing = data['facing']
        self._trailing = data['trailing']

    @staticmethod
    def get_template(is_array):
        return prepare_template(signal_structure, is_array)

    @property
    def name(self):
        return self._name

    @property
    def distance(self):
        return self._distance

    @property
    def district(self):
        return self._district

    @property
    def type(self):
        return self._type

    @property
    def facing(self):
        return self._facing

    @property
    def trailing(self):
        return self._trailing


class Track(yaml.YAMLObject):

    yaml_tag = u'!Track'
    yaml_flow_style = False

    def __init__(self, data):
        self._name = data['name']
        self._start = data['start']
        self._end = data['end']
        self._type = data['type']

    @staticmethod
    def get_template(is_array):
        return prepare_template(track_structure, is_array)

    @property
    def name(self):
        return self._name

    @property
    def start(self):
        return self._start

    @property
    def end(self):
        return self._end

    @property
    def type(self):
        return self._type
