from PIL import Image
import numpy as np


def identity(x):
    return x


def sample_hsv_cone(hue_steps=26, saturation_step_depth=2, value_step_depth=2, s_sampler=identity, v_sampler=identity):
    result_list = []
    delta_h = 360.0 / hue_steps

    for h_step in range(0, hue_steps):
        result_list.extend(
            sample_hue_triangle(h_step * delta_h, saturation_step_depth, value_step_depth, s_sampler, v_sampler))
    return result_list


def sample_hue_triangle(h, saturation_step_depth=2, value_step_depth=2, s_sampler=identity, v_sampler=identity):
    result_list = []
    saturation_steps = depth_to_steps(saturation_step_depth)
    value_steps = depth_to_steps(value_step_depth)
    delta_s = delta_with_borders(saturation_steps)
    delta_v = delta_with_borders(value_steps)

    # Start at 1 because greyscale repeats itself otherwise
    for s_step in range(1, saturation_steps):
        s = s_sampler(delta_s * s_step)
        for v_step in range(1, value_steps):
            v = v_sampler(delta_v * v_step)
            result_list.append([h, s, v])
    return result_list


def sample_grayscale_line(value_step_depth=2, v_sampler=identity):
    result_list = []
    value_steps = depth_to_steps(value_step_depth)
    delta_v = delta_with_borders(value_steps)
    for v_step in range(0, value_steps):
        result_list.append([0, 0, v_sampler(delta_v * v_step)])
    return result_list


def depth_to_steps(depth):
    return 2 ** depth + 1


def delta_with_borders(x):
    return 1.0 / (x - 1)


def hsv_to_rgb(hsv):
    (h, s, v) = hsv
    (r, g, b) = (0, 0, 0)
    c = v * s
    x = c * (1 - abs(h / 60 % 2 - 1))
    m = v - c

    if 0 <= h < 60:
        (r, g, b) = (c, x, 0)
    elif 60 <= h < 120:
        (r, g, b) = (x, c, 0)
    elif 120 <= h < 180:
        (r, g, b) = (0, c, x)
    elif 180 <= h < 240:
        (r, g, b) = (0, x, c)
    elif 240 <= h < 300:
        (r, g, b) = (x, 0, c)
    elif 300 <= h < 360:
        (r, g, b) = (c, 0, x)

    (r, g, b) = (r + m, g + m, b + m)
    (r, g, b) = (r * 255, g * 255, b * 255)
    return [r, g, b]


def map_round(lst):
    return list(map(round, lst))


def rounded_colors(lst):
    return list(map(map_round, lst))


if __name__ == '__main__':
    s_step_depth = 2
    v_step_depth = 2
    h_steps = 72

    v_samp = identity
    s_samp = identity

    cone = sample_hsv_cone(h_steps, s_step_depth, v_step_depth, s_samp, v_samp)
    line = sample_grayscale_line(v_step_depth, v_samp)

    print("HSV color cone:")
    print(cone)
    print("HSV grayscale line:")
    print(line)
    print("RGB color cone:")
    rgb_cone = list(map(hsv_to_rgb, cone))
    print(rounded_colors(rgb_cone))
    print("RGB grayscale line:")
    rgb_line = list(map(hsv_to_rgb, line))
    print(rounded_colors(rgb_line))

    s_steps = 2 ** v_step_depth

    img_arr = np.zeros([s_steps, int(len(cone) / s_steps) + len(line), 3],
                       dtype=np.uint8)

    for i in range(0, int(len(rgb_cone) / s_steps)):
        for j in range(0, s_steps):
            img_arr[j, i] = rgb_cone[i * s_steps + j]

    for i in range(0, len(rgb_line)):
        j = int(len(rgb_cone) / s_steps) + i
        img_arr[:, j:j + 1] = rgb_line[i]

    img = Image.fromarray(img_arr)
    img.save('out.png')
