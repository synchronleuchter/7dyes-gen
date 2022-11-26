import sys


def color_id(rgb_color, pigment=False):
    id_suffix = f'{rgb_color[0]}_{rgb_color[1]}_{rgb_color[2]}'
    type_tag = 'Pigment' if pigment else 'Dye'
    return f"mod{type_tag}Rgb_{id_suffix}"


def generate_file(filename, module, hsv_cone, rgb_cone, hsv_line, rgb_line, colors_per_hue):
    original_stdout = sys.stdout

    with open(filename, 'w') as file:
        sys.stdout = file
        print(module.prefix)
        for i in range(0, len(rgb_cone)):
            print(module.body(hsv_cone[i], list(map(round, rgb_cone[i])), i % colors_per_hue == colors_per_hue - 1))
        for i in range(0, len(rgb_line)):
            print(module.body(hsv_line[i], list(map(round, rgb_line[i]))))
        print(module.suffix, end='')

    sys.stdout = original_stdout
