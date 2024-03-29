import os
import sys

import colors

out_dir = '7dyes/'
config_dir = out_dir + 'Config/'


def id_suffix(rgb_color) :
    return f'{rgb_color[0]}_{rgb_color[1]}_{rgb_color[2]}'


def color_id(rgb_color, pigment=False):
    type_tag = 'Pigment' if pigment else 'Dye'
    return f"mod{type_tag}Rgb_{id_suffix(rgb_color)}"


def pigment_dust_id(rgb_color):
    # Note: This must be a pigment color to begin with; performs no checks.
    return f'pigment_dust_rgb{id_suffix(rgb_color)}'


def black_id():
    return color_id([0, 0, 0])


def white_id():
    return color_id([255, 255, 255])


def generate_file(filename, module, hsv_cone, rgb_cone, hsv_line, rgb_line, colors_per_hue, v_steps):
    original_stdout = sys.stdout
    rgb_rd = list(map(colors.map_round, rgb_cone))
    rgb_ld = list(map(colors.map_round, rgb_line))

    if not os.path.exists(out_dir):
        os.mkdir(out_dir)
    if not os.path.exists(config_dir):
        os.mkdir(config_dir)

    with open(config_dir + filename, 'w') as file:
        sys.stdout = file
        print(module.prefix)
        for i in range(0, len(rgb_cone)):
            body = module.body(i, hsv_cone, rgb_rd, rgb_ld, v_steps, colors_per_hue, False, i % colors_per_hue == colors_per_hue - 1)
            if body != '':
                print(body)
        for i in range(0, len(rgb_line)):
            body = module.body(i, hsv_line, rgb_rd, rgb_ld, v_steps, colors_per_hue, True)
            if body != '':
                print(body)
        print(module.suffix, end='')

    sys.stdout = original_stdout


def generate_mod_info():
    mod_info = \
'''<?xml version="1.0" encoding="UTF-8" ?>
<xml>
<ModInfo>
    <Name value="7 Dyes to dye for" />
    <Description value="Generated mod that potentially adds heaps of dyes with its own dye mixing recipes. 'Open' dye bottles to turn them into pigment powder." />
    <Author value="Synchronleuchter" />
    <Version value="1.5" />
</ModInfo>
</xml>
'''
    original_stdout = sys.stdout
    if not os.path.exists(out_dir):
        os.mkdir(out_dir)
    with open(out_dir + 'ModInfo.xml', 'w') as file:
        sys.stdout = file
        print(mod_info)
    sys.stdout = original_stdout
