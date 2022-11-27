from text_output import common
import colors

prefix = '''<configs>'''

suffix = '''</configs>'''


def body(i, hsv_space, rgb_cone, rgb_line, v_steps, colors_per_hue, grayscale, pigment=False):
    gs_lookup = rgb_cone if not grayscale else rgb_line
    des_gs = gs_lookup
    dev_gs = gs_lookup
    rgb_color = gs_lookup[i]
    des_idx = colors.desaturated_index(i, v_steps, colors_per_hue)
    dev_idx = colors.devalued_index(i, v_steps, colors_per_hue)

    if grayscale:
        des_idx = i + 1
        dev_idx = i - 1
    else:
        if des_idx < 0:
            des_idx *= -1
            des_gs = rgb_line
        if dev_idx < 0:
            dev_idx = 0
            dev_gs = rgb_line

    retval = ''

    # Desaturate by one (except if that yields white. Why would you mix white and X to yield more white?)
    # (I mean, this is a technical workaround, really.)
    if common.color_id(rgb_color, pigment) != common.white_id():
        desaturated = des_gs[des_idx]
        if common.color_id(desaturated) != common.white_id():
            # Do not waste pigments by turning them into gray.
            if colors.is_grayscale(rgb_color) or not colors.is_grayscale(desaturated):
                retval += \
f'''<append xpath="/recipes"><recipe name="{common.color_id(desaturated)}" count="2" craft_time="1">
    <ingredient name="{common.color_id(rgb_color, pigment)}" count="1"/>
    <ingredient name="{common.white_id()}" count="1"/>
</recipe></append>
'''

    # Devalue by one (except if that yields black. Why would you mix black and X to yield more black?)
    # (I mean, this is a technical workaround, really.)
    if common.color_id(rgb_color, pigment) != common.black_id():
        devalued = dev_gs[dev_idx]
        if common.color_id(devalued) != common.black_id():
            retval += \
f'''<append xpath="/recipes"><recipe name="{common.color_id(devalued)}" count="2" craft_time="1">
	<ingredient name="{common.color_id(rgb_color, pigment)}" count="1"/>
	<ingredient name="{common.black_id()}" count="1"/>
</recipe></append>
'''

    # Reset pigmentation: Cook a dye to concentrate it. Yes, this allows infinite replication. This is intended.
    # We do it this way because 7dtd's recipe graph must be acyclic.
    if pigment:
        corresponding_pigment = rgb_cone[colors.corresponding_pigment_index(i, colors_per_hue)]
        pigment_dust_id = common.pigment_dust_id(corresponding_pigment)
        retval += \
f'''<append xpath="/recipes"><recipe name="{common.color_id(corresponding_pigment, True)}" craft_area="chemistryStation" count="1" craft_time="1">
	<ingredient name="{pigment_dust_id}" count="1"/>
	<ingredient name="drinkJarRiverWater" count="1"/>
</recipe></append>
'''
        retval += \
f'''<append xpath="/recipes"><recipe name="{common.color_id(corresponding_pigment, True)}" craft_area="campfire" count="1" craft_time="3">
	<ingredient name="{pigment_dust_id}" count="1"/>
	<ingredient name="drinkJarRiverWater" count="1"/>
</recipe></append>
'''
    # Generate static recipes for black and white dye because they are the lifeblood of transforming dyes.
    if common.color_id(rgb_color, pigment) == common.black_id():
        retval += \
f'''<append xpath="/recipes"><recipe name="{common.black_id()}" craft_area="chemistryStation" count="1" craft_time="1">
    <ingredient name="resourceCoal" count="10"/>
    <ingredient name="drinkJarRiverWater" count="1"/>
</recipe></append>
'''
        retval += \
f'''<append xpath="/recipes"><recipe name="{common.black_id()}" craft_area="campfire" count="1" craft_time="3">
    <ingredient name="resourceCoal" count="10"/>
    <ingredient name="drinkJarRiverWater" count="1"/>
</recipe></append>
'''
    if common.color_id(rgb_color, pigment) == common.white_id():
        retval += \
f'''<append xpath="/recipes"><recipe name="{common.white_id()}" craft_area="chemistryStation" count="1" craft_time="1">
    <ingredient name="resourcePotassiumNitratePowder" count="10"/>
    <ingredient name="drinkJarRiverWater" count="1"/>
</recipe></append>
'''
        retval += \
f'''<append xpath="/recipes"><recipe name="{common.white_id()}" craft_area="campfire" count="1" craft_time="3">
    <ingredient name="resourcePotassiumNitratePowder" count="10"/>
    <ingredient name="drinkJarRiverWater" count="1"/>
</recipe></append>
'''
    return retval
