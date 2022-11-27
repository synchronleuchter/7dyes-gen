from text_output import common


prefix = 'Key,File,Type,UsedInMainMenu,NoTranslate,english,Context / Alternate Text,german,latam,french,italian,japanese,koreana,polish,brazilian,russian,turkish,schinese,tchinese,spanish'

suffix = ''


def body(i, hsv_space, rgb_cone, rgb_line, v_steps, colors_per_hue, grayscale, pigment=False):
    # TODO: Nicknames for dyes? Have a dictionary from rgb or hsv to names and append in braces for better search?
    # Over-engineered variation: Intervals for names? Quadrants? (Pure, Dark, Pale, Washed-out) x (Red, Orange,...)
    # Even more over-engineering: Overrides (dark orange = brown)?
    rgb_color = rgb_cone[i] if not grayscale else rgb_line[i]
    hsv_color = hsv_space[i] if not grayscale else hsv_space[i]
    color = f'{round(hsv_color[0]):03d}-{round(hsv_color[1] * 100):03d}-{round(hsv_color[2] * 100):03d}'
    dye_name = f'7Dyes[tm] Dye: {color} (Pigment)' if pigment else f'7Dyes[tm] Dye: {color}'
    if grayscale:
        dye_name = f'7Dyes[tm] Grayscale Dye: {round(hsv_color[2] * 100):03d}'
    retval = f'''{common.color_id(rgb_color, pigment)},item_modifiers,mod,,,{dye_name},,{dye_name},{dye_name},{dye_name},{dye_name},{dye_name},{dye_name},{dye_name},{dye_name},{dye_name},{dye_name},{dye_name},{dye_name},{dye_name}'''

    if pigment:
        pigment_dust_id = common.pigment_dust_id(rgb_color)
        pigment_name = f'7Dyes[tm] Pigment Powder: {round(hsv_color[0]):03d}'
        retval += f'''\n{pigment_dust_id},items,Item,,,{pigment_name},,{pigment_name},,{pigment_name},,{pigment_name},,{pigment_name},,{pigment_name},,{pigment_name},,{pigment_name},,{pigment_name},,{pigment_name},,{pigment_name},,{pigment_name},,{pigment_name},,{pigment_name}\n'''

    return retval
