from . import vertex_colors

_targets = [
    vertex_colors
]


def get_target(id):
    for target in _targets:
        if target.target_id == id:
            return target

    raise Exception("Target not found: " + id)


def get_targets_enum():
    enum_list = []
    i = 0
    for target in _targets:
        enum_list.append((target.target_id, target.name, target.description, i))
        i += 1

    return enum_list
