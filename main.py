from PIL import Image
import numpy as np
import colors
from text_output import item_modifiers, loot, common, localization, recipes


def save_preview_image():
    v = 2 ** v_step_depth
    img_arr = np.zeros([v, int(len(hsv_cone) / v) + len(hsv_line), 3],
                       dtype=np.uint8)

    for i in range(0, int(len(rgb_cone) / v)):
        for j in range(0, v):
            img_arr[j, i] = rgb_cone[i * v + j]

    for i in range(0, len(rgb_line)):
        j = int(len(rgb_cone) / v) + i
        img_arr[:, j:j + 1] = rgb_line[i]

    img = Image.fromarray(img_arr)
    img.save('preview.png')


if __name__ == '__main__':
    s_step_depth = 2
    v_step_depth = 2
    h_steps = 12

    # Since we're sampling a triangle in a square space, we might choose differing sample depths.
    v_samp = colors.identity
    s_samp = lambda x: x ** (1/1.5)

    hsv_cone = colors.sample_hsv_cone(h_steps, s_step_depth, v_step_depth, s_samp, v_samp)
    hsv_line = colors.sample_grayscale_line(v_step_depth, v_samp)

    rgb_cone = list(map(colors.hsv_to_rgb, hsv_cone))
    rgb_line = list(map(colors.hsv_to_rgb, hsv_line))
    save_preview_image()

    colors_per_hue = 2 ** s_step_depth * 2 ** v_step_depth

    common.generate_file('item_modifiers.xml', item_modifiers, hsv_cone, rgb_cone, hsv_line, rgb_line, colors_per_hue)
    common.generate_file('loot.xml', loot, hsv_cone, rgb_cone, hsv_line, rgb_line, colors_per_hue)
    common.generate_file('Localization.txt', localization, hsv_cone, rgb_cone, hsv_line, rgb_line, colors_per_hue)
    common.generate_file('recipes.xml', recipes, hsv_cone, rgb_cone, hsv_line, rgb_line, colors_per_hue)

    # TODO: Transition Recipes
    # TODO: Recipe for white
    # TODO: Recipe for black
