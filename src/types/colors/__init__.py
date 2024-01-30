from . import generated

_colors = [
    generated
]


def get_color(id):
    for color in _colors:
        if color.color_id == id:
            return color

    raise Exception("Source not found: " + id)


def get_color_enum():
    enum_list = []
    i = 0
    for color in _colors:
        enum_list.append((color.color_id, color.name, color.description, i))
        i += 1

    return enum_list

