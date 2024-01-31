color_id = 'COLOR_PALETTE'
name = 'Palette'
description = "The color palette is specified by the user"


def get_colors(props):
    if not props.colors_color_palette_palette:
        return []

    return list(map(lambda x: x.color, props.colors_color_palette_palette.colors))


def get_count(props):
    if not props.colors_color_palette_palette:
        return 0

    return len(props.colors_color_palette_palette.colors)


def render_ui(context, layout, props):
    layout.template_ID(props, "colors_color_palette_palette")
    if props.colors_color_palette_palette:
        row = layout.column()
        row.enabled = False
        row.template_palette(props, "colors_color_palette_palette", color=True)
