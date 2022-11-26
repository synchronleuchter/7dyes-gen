from text_output import common


prefix = '''<configs>'''

suffix = '''</configs>'''


def body(hsv_color, rgb_color, pigment=False):
    return f'''<append xpath="/lootcontainers/lootgroup[@name='dyes']">	<item name="{common.color_id(rgb_color, pigment)}"/></append>'''