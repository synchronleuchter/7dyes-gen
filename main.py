from PIL import Image
import numpy as np
import os
import colors
from text_output import item_modifiers, loot, common, localization, recipes, items


def save_preview_image(cone, line, name='preview.png'):
    out_dir = 'previews/'
    if not os.path.exists(out_dir):
        os.mkdir(out_dir)

    v = 2 ** v_step_depth
    img_arr = np.zeros([v, int(len(hsv_cone) / v) + len(hsv_line), 3],
                       dtype=np.uint8)

    for i in range(0, int(len(cone) / v)):
        for j in range(0, v):
            img_arr[j, i] = cone[i * v + j]

    for i in range(0, len(line)):
        j = int(len(cone) / v) + i
        img_arr[:, j:j + 1] = line[i]

    img = Image.fromarray(img_arr)
    img.save(out_dir + name)


if __name__ == '__main__':
    # These are exponential steps. I had a binary subdivision sampling in mind, but then noticed that there would
    # be no backwards steps (anti-s, anti-v). This (and the grayscale optimization) explain the somewhat weird
    # sampling.
    s_step_depth = 4
    v_step_depth = 4
    h_steps = 48

    # If you want to shift all the hue sample, you can do that here.
    h_offset_degrees = 0.0

    # Since we're sampling a triangle in a square space, we might choose differing sample depths.
    # This has effects on which parts of the color space are sampled more finely. Experiment with different functions!
    # I tried sin/cos and powers thereof, some roots etc. and found to like saturation to be sampled with x**(1/1.5).
    v_samp = colors.identity
    s_samp = lambda x: x ** (1/1.5)

    # This is our cone with colors that have a hue. We omit grayscale versions as an optimization.
    hsv_cone = colors.sample_hsv_cone(h_steps, s_step_depth, v_step_depth, s_samp, v_samp, h_offset_degrees)
    # This is a grayscale line. No need to have tons of "different" grayscale colors as hue plays no role.
    hsv_line = colors.sample_grayscale_line(v_step_depth, v_samp)

    rgb_cone = list(map(colors.hsv_to_rgb, hsv_cone))
    rgb_line = list(map(colors.hsv_to_rgb, hsv_line))
    save_preview_image(rgb_cone, rgb_line)

    colors_per_hue = 2 ** s_step_depth * 2 ** v_step_depth

    common.generate_file('item_modifiers.xml', item_modifiers, hsv_cone, rgb_cone, hsv_line, rgb_line, colors_per_hue, 2 ** v_step_depth)
    common.generate_file('loot.xml', loot, hsv_cone, rgb_cone, hsv_line, rgb_line, colors_per_hue, 2 ** v_step_depth)
    common.generate_file('Localization.txt', localization, hsv_cone, rgb_cone, hsv_line, rgb_line, colors_per_hue, 2 ** v_step_depth)
    common.generate_file('recipes.xml', recipes, hsv_cone, rgb_cone, hsv_line, rgb_line, colors_per_hue, 2 ** v_step_depth)
    common.generate_file('items.xml', items, hsv_cone, rgb_cone, hsv_line, rgb_line, colors_per_hue,
                         2 ** v_step_depth)
    common.generate_mod_info()

    # Debugging purposes: For each color, show the next less saturated one. Think of this as a recipe mapping table.
    desaturated_cone = []
    for i in range(0, len(rgb_cone)):
        idx = colors.desaturated_index(i, 2 ** v_step_depth, colors_per_hue)
        rgb = rgb_cone[idx] if idx >= 0 else rgb_line[-idx]
        desaturated_cone.append(rgb)

    # Terminology alert! We'll make grayscale colors "brighter" when mixing them with white dye.
    brightened_line = []
    for i in range(0, len(rgb_line) - 1):
        brightened_line.append(rgb_line[i + 1])
    brightened_line.append(255.0)
    save_preview_image(desaturated_cone, brightened_line, 'desaturated.png')

    # Debugging purposes: For each color, show the next darker one. Think of this as a recipe mapping table.
    devalued_cone = []
    for i in range(0, len(rgb_cone)):
        idx = colors.devalued_index(i, 2 ** v_step_depth, colors_per_hue)
        rgb = rgb_cone[idx] if idx >= 0 else rgb_line[0]
        devalued_cone.append(rgb)

    devalued_line = [0.0]
    for i in range(1, len(rgb_line)):
        devalued_line.append(rgb_line[i - 1])

    save_preview_image(devalued_cone, devalued_line, 'devalued.png')

    # Debugging purposes: For each color, show its pure pigment.
    corresponding_pigments = []
    for i in range(0, len(rgb_cone)):
        idx = colors.corresponding_pigment_index(i, colors_per_hue)
        rgb = rgb_cone[idx] if idx is not None else [0.0, 0.0, 0.0]
        corresponding_pigments.append(rgb)

    save_preview_image(corresponding_pigments, rgb_line, 'pigments.png')