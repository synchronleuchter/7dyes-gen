from text_output import common


prefix = 'Key,File,Type,UsedInMainMenu,NoTranslate,english,Context / Alternate Text,german,latam,french,italian,japanese,koreana,polish,brazilian,russian,turkish,schinese,tchinese,spanish'

suffix = ''


def body(hsv_color, rgb_color, pigment=False):
    color = f'{round(hsv_color[0]):03d}-{round(hsv_color[1] * 100):03d}-{round(hsv_color[2] * 100):03d}'
    dye_name = f'7Dyes[tm] Dye: {color} (Pigment)' if pigment else f'7Dyes[tm] Dye: {color}'
    if hsv_color[1] == 0.0:
        dye_name = f'7Dyes[tm] Grayscale Dye: {round(hsv_color[2] * 100):03d}'
    return f'''{common.color_id(rgb_color, pigment)},item_modifiers,mod,,,{dye_name},,{dye_name},{dye_name},{dye_name},{dye_name},{dye_name},{dye_name},{dye_name},{dye_name},{dye_name},{dye_name},{dye_name},{dye_name},{dye_name}'''