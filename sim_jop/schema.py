#!/usr/bin/env python3

from sim_jop.railway.elements import Area, Meta, District, Entrypoint, Junction, Signal, Track


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
