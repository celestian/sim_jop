#!/usr/bin/env python3

import logging
import yaml

from sim_jop.railway.elements import Area, Meta, District, Entrypoint, Junction, Signal, Track

LOG = logging.getLogger(__name__)


class Schema(yaml.YAMLObject):

    yaml_tag = u'!Schema'
    yaml_flow_style = False

    def __init__(self, source_file):

        self.source_file = source_file
        self.elements = {}

        self.area = None
        self.meta = None
        self.districts = []
        self.entrypoints = []
        self.junctions = []
        self.signals = []
        self.tracks = []

        self._load_elements()
        self._check_integrity()
        self._create_connections()

    def _load_elements(self):

        LOG.info('Loading file "{}"'.format(self.source_file))
        with open(self.source_file, 'r') as source:
            data = yaml.safe_load(source)

        if 'area' in data:
            self.area = Area(data['area'])
        else:
            LOG.error('area is missing')
            exit(0)

        if 'meta' in data:
            self.meta = Meta(data['meta'])
        else:
            loggign.error('meta is missing')
            exit(0)

        LOG.info('Schema {} by {}'.format(self.area.name, self.meta.author))
        LOG.info('Version {}'.format(self.meta.version))

        if 'district' in data:
            for item in data['district']:
                district = District(item)
                self.elements[district.name] = district
                self.districts.append(district)

        if 'entrypoint' in data:
            for item in data['entrypoint']:
                entrypoint = Entrypoint(item)
                self.elements[entrypoint.name] = entrypoint
                self.entrypoints.append(entrypoint)

        if 'junction' in data:
            for item in data['junction']:
                junction = Junction(item)
                self.elements[junction.name] = junction
                self.junctions.append(junction)

        if 'signal' in data:
            for item in data['signal']:
                signal = Signal(item)
                self.elements[signal.name] = signal
                self.signals.append(signal)

        if 'track' in data:
            for item in data['track']:
                track = Track(item)
                self.elements[track.name] = track
                self.tracks.append(track)

        LOG.info('Schema contains {} elements'.format(len(self.elements)))

    def _check_integrity(self):

        keys = list(self.elements.keys())
        for key in keys:
            element = self.elements[key]
            if isinstance(element, Entrypoint):
                if element.connection not in keys:
                    LOG.error('{} is missing connection element {}'.format(
                        element.name, element.connection))
                    exit(0)
            if isinstance(element, (Entrypoint, Junction, Signal)):
                if element.district not in keys:
                    LOG.error('{} is missing district element {}'.format(
                        element.name, element.district))
                    exit(0)
            if isinstance(element, (Junction, Signal)):
                if element.facing not in keys:
                    LOG.error('{} is missing facing element {}'.format(
                        element.name, element.facing))
                    exit(0)
                if element.trailing not in keys:
                    LOG.error('{} is missing trailing element {}'.format(
                        element.name, element.trailing))
                    exit(0)
            if isinstance(element, Junction):
                if element.sidding not in keys:
                    LOG.error('{} is missing sidding element {}'.format(
                        element.name, element.sidding))
                    exit(0)
            if isinstance(element, Track):
                if element.start_connection not in keys:
                    LOG.error('{} is missing start_connection element {}'.format(
                        element.name, element.start_connection))
                    exit(0)
                if element.end_connection not in keys:
                    LOG.error('{} is missing end_connection element {}'.format(
                        element.name, element.end_connection))
                    exit(0)

        LOG.info('Succesful integrity check')

    def get_distances(self):

        distances = []
        for element in self.junctions:
            if element.distance not in distances:
                distances.append(element.distance)
        for element in self.signals:
            if element.distance not in distances:
                distances.append(element.distance)
        for element in self.tracks:
            if element.start not in distances:
                distances.append(element.start)
            if element.end not in distances:
                distances.append(element.end)

        return sorted(distances)

    def _create_connections(self):

        keys = list(self.elements.keys())
        for key in keys:
            element = self.elements[key]
            if isinstance(element, Entrypoint):
                if isinstance(element.connection, str):
                    element.connection = self.elements[element.connection]
            if isinstance(element, (Entrypoint, Junction, Signal)):
                if isinstance(element.district, str):
                    element.district = self.elements[element.district]
            if isinstance(element, (Junction, Signal)):
                if isinstance(element.facing, str):
                    element.facing = self.elements[element.facing]
                if isinstance(element.trailing, str):
                    element.trailing = self.elements[element.trailing]
            if isinstance(element, Junction):
                if isinstance(element.sidding, str):
                    element.sidding = self.elements[element.sidding]
            if isinstance(element, Track):
                if isinstance(element.start_connection, str):
                    element.start_connection = self.elements[element.start_connection]
                if isinstance(element.end_connection, str):
                    element.end_connection = self.elements[element.end_connection]

        LOG.info('Connections created')

    def add_track(self, element):

        def add_connection(new_element, element):

            before = new_element.start_connection
            after = new_element.end_connection

            if isinstance(element, Signal):
                if before == element:
                    element.facing = element.facing if element.facing != after else new_element
                    element.trailing = element.trailing if element.trailing != after else new_element
                if after == element:
                    element.facing = element.facing if element.facing != before else new_element
                    element.trailing = element.trailing if element.trailing != before else new_element
            else:
                raise Exception.NotImplementedError(
                    'Please, open issue to implement add_connection for {}'.format(
                        type(element)))

        if element.start_connection not in self.elements:
            LOG.error('Can not add element "{}" into schema "{}": "{}" is missing'.format(
                element.name, self.area.name, element.start_connection.name))
            raise Exception('Element is missing')

        if element.end_connection not in self.elements:
            LOG.error('Can not add element "{}" into schema "{}": "{}" is missing'.format(
                element.name, self.area.name, element.end_connection.name))
            raise Exception('Element is missing')

        if element not in self.elements:
            self.elements[element.name] = element
        else:
            LOG.error(
                'Can not add element "{}" into schema "{}": element already exists'.format(
                    element.name, self.area.name))
            raise Exception('Element already exists')

        add_connection(element, element.start_connection)
        add_connection(element, element.end_connection)

        self.tracks.append(element)


def prepare_schema(output_file):

    district_number = int(input('Počet železničních obvodů (district): '))
    entrypoint_number = int(input('Počet vstupních uzlů (entrypoint): '))
    junction_number = int(input('Počet výhybek (junction): '))
    signal_number = int(input('Počet návěstidel (signal): '))
    track_number = int(input('Počet kolejí (track): '))

    with open(output_file, 'w') as outfile:
        outfile.write('area:\n')
        outfile.write(Area.get_template(is_array=False))

        outfile.write('meta:\n')
        outfile.write(Meta.get_template(is_array=False))

        outfile.write('district:\n')
        for _ in range(district_number):
            outfile.write(District.get_template(is_array=True))

        outfile.write('entrypoint:\n')
        for _ in range(entrypoint_number):
            outfile.write(Entrypoint.get_template(is_array=True))

        outfile.write('junction:\n')
        for _ in range(junction_number):
            outfile.write(Junction.get_template(is_array=True))

        outfile.write('signal:\n')
        for _ in range(signal_number):
            outfile.write(Signal.get_template(is_array=True))

        outfile.write('track:\n')
        for _ in range(track_number):
            outfile.write(Track.get_template(is_array=True))
