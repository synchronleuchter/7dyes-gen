from text_output import common


prefix = '''<configs>'''

suffix = '''</configs>'''


def body(hsv_color, rgb_color, pigment=False):
    # TODO: Replace placeholder recipes
    return f'''<append xpath="/recipes"><recipe name="{common.color_id(rgb_color, pigment)}" count="1" craft_time="1">
	<ingredient name="modDyeRed" count="1"/>
</recipe></append>'''