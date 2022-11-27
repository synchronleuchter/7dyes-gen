import os
import sys

import colors


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
    out_dir = 'out/'

    if not os.path.exists(out_dir):
        os.mkdir(out_dir)
    with open(out_dir + filename, 'w') as file:
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
