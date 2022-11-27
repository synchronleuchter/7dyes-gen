from text_output import common


prefix = 'Key,File,Type,UsedInMainMenu,NoTranslate,english,Context / Alternate Text,german,latam,french,italian,japanese,koreana,polish,brazilian,russian,turkish,schinese,tchinese,spanish'

s_normal_dye = '"A pre-mixed 7Dyes[tm] dye bottle. This can be mixed further with licensed 7Dyes[tm] black or white dyes.\\n\\nWhen opening the bottle, beware that 7Dyes[tm] dyes take far less than 7 days to oxidize. You can turn the dye into pure pigment powder which you can in turn solve in water to make new, bright dye."'
s_pigment = '"A patented 7Dyes[tm] pigment dye bottle. This dye is so intense, you could probably dilute it a million times and still hurt your eyes from how intense the color is."'
s_grayscale = 'A 7Dyes[tm] Grayscale dye bottle. This can be brightened or darkened with licensed 7Dyes[tm] black or white dyes.'
s_white = 'The purest 7Dyes[tm] white dye. Use this to desaturate (or brighten) other licensed 7Dyes[tm] dyes.'
s_black = 'The darkest 7Dyes[tm] black dye. Use this to darken other licensed 7Dyes[tm] dyes.'
s_powder = '"Oxidized 7Dyes[tm] pigment powder. This is what happens if 7Dyes[tm] dyes get (far) less than 7 days to dry.\\n\\nNo worries! If you want to create 7Dyes pigment dye, just add water over some fire! You can even create more pigment by progressively diluting and cooking dyes this way."'
suffix = f'''mod7DyesGroupDesc,item_modifiers,mod,,,{s_normal_dye},,{s_normal_dye},{s_normal_dye},{s_normal_dye},{s_normal_dye},{s_normal_dye},{s_normal_dye},{s_normal_dye},{s_normal_dye},{s_normal_dye},{s_normal_dye},{s_normal_dye},{s_normal_dye},{s_normal_dye}
mod7DyesGroupDescPigment,item_modifiers,mod,,,{s_pigment},,{s_pigment},{s_pigment},{s_pigment},{s_pigment},{s_pigment},{s_pigment},{s_pigment},{s_pigment},{s_pigment},{s_pigment},{s_pigment},{s_pigment},{s_pigment}
mod7DyesGroupDescGrayscale,item_modifiers,mod,,,{s_grayscale},,{s_grayscale},{s_grayscale},{s_grayscale},{s_grayscale},{s_grayscale},{s_grayscale},{s_grayscale},{s_grayscale},{s_grayscale},{s_grayscale},{s_grayscale},{s_grayscale},{s_grayscale}
mod7DyesGroupDescGrayscaleWhite,item_modifiers,mod,,,{s_white},,{s_white},{s_white},{s_white},{s_white},{s_white},{s_white},{s_white},{s_white},{s_white},{s_white},{s_white},{s_white},{s_white}
mod7DyesGroupDescGrayscaleBlack,item_modifiers,mod,,,{s_black},,{s_black},{s_black},{s_black},{s_black},{s_black},{s_black},{s_black},{s_black},{s_black},{s_black},{s_black},{s_black},{s_black}
resource7DyesPigmentPowder,item_modifiers,mod,,,{s_powder},,{s_powder},{s_powder},{s_powder},{s_powder},{s_powder},{s_powder},{s_powder},{s_powder},{s_powder},{s_powder},{s_powder},{s_powder},{s_powder}'''


hue_dict = {
    0: 'Red',
    30: 'Orange',
    60: 'Yellow',
    90: 'Lime',
    120: 'Green',
    150: 'Mint',
    180: 'Cyan',
    210: 'Aqua',
    240: 'Blue',
    270: 'Purple',
    300: 'Magenta',
    330: 'Berry'
}


def around(hue, reference_hue, delta=5.0):
    return (hue - delta) % 360.0 < reference_hue <= (hue + delta) % 360.0


def special_name_suffix(rgb_col, hsv_color):
    retval = ''
    hue = hsv_color[0]
    sat = hsv_color[1]
    val = hsv_color[2]

    if rgb_col == [0.0, 0.0, 0.0]:
        return '(Black)'

    if rgb_col == [255.0, 255.0, 255.0]:
        return '(White)'

    if 0.0 < sat <= 0.25 and val >= 0.5:
        retval += '(Pale '
    elif 0.0 < sat <= 0.25 and val < 0.5:
        retval += '(Washed-out '
    elif 0.25 < sat and val < 0.5:
        retval += '(Dark '
    elif 1.0 == sat and 1.0 == val:
        retval += '(Pure '

    # FIXME: This doesn't choose the closest match
    if retval != '':
        for key in hue_dict.keys():
            if around(hue, key):
                retval += hue_dict[key] + ')'
                break

    if retval != '' and retval[-1] != ')':
        retval = ''

    return retval


def body(i, hsv_space, rgb_cone, rgb_line, v_steps, colors_per_hue, grayscale, pigment=False):
    rgb_color = rgb_cone[i] if not grayscale else rgb_line[i]
    hsv_color = hsv_space[i] if not grayscale else hsv_space[i]
    color = f'{round(hsv_color[0]):03d}-{round(hsv_color[1] * 100):03d}-{round(hsv_color[2] * 100):03d}'
    dye_name = f'7Dyes[tm] Dye: {color} (Pigment)' if pigment else f'7Dyes[tm] Dye: {color}'
    if grayscale:
        dye_name = f'7Dyes[tm] Grayscale Dye: {round(hsv_color[2] * 100):03d}'

    dye_name += ' ' + special_name_suffix(rgb_color, hsv_color)

    retval = f'''{common.color_id(rgb_color, pigment)},item_modifiers,mod,,,{dye_name},,{dye_name},{dye_name},{dye_name},{dye_name},{dye_name},{dye_name},{dye_name},{dye_name},{dye_name},{dye_name},{dye_name},{dye_name},{dye_name}'''

    if pigment:
        pigment_dust_id = common.pigment_dust_id(rgb_color)
        pigment_name = f'7Dyes[tm] Pigment Powder: {round(hsv_color[0]):03d}'
        retval += f'''\n{pigment_dust_id},items,Item,,,{pigment_name},,{pigment_name},,{pigment_name},,{pigment_name},,{pigment_name},,{pigment_name},,{pigment_name},,{pigment_name},,{pigment_name},,{pigment_name},,{pigment_name},,{pigment_name},,{pigment_name},,{pigment_name}\n'''

    return retval
