from text_output import common


prefix = '''<configs>'''

suffix = '''</configs>'''


def body(i, hsv_cone, rgb_cone, rgb_line, v_steps, colors_per_hue, grayscale, pigment=False):
    rgb_color = rgb_cone[i] if not grayscale else rgb_line[i]
    return f'''<append xpath="/lootcontainers/lootgroup[@name='dyes']">	<item name="{common.color_id(rgb_color, pigment)}"/></append>'''