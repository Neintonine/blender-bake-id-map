import colorsys

color_id = 'GENERATED'
name = 'Generated'
description = 'The colors get generated on-the-fly'

MAX_BRIGHTNESS_STEPS = 8
MAX_SATURATION_STEPS = 8
MAX_HUES_STEPS = 8

def get_colors(props):
    return gen_colors()


def get_count(props):
    return len(gen_colors())


def gen_colors():
    colors = []
    for brightnessStep in range(0, MAX_BRIGHTNESS_STEPS):
        v = 1 - (brightnessStep / MAX_BRIGHTNESS_STEPS)
        for satuationStep in range(0, MAX_SATURATION_STEPS):
            s = 1 - (satuationStep / MAX_SATURATION_STEPS)
            for hueStep in range(0, MAX_HUES_STEPS):
                h = hueStep / MAX_HUES_STEPS

                color = colorsys.hsv_to_rgb(h, s, v)
                colors.append(color)

    return colors