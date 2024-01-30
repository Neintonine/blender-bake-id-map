from . sources import material_index as source_mat_index

from . targets import vertex_colors as target_vertex_colors

_sources = [
    source_mat_index
]

_targets = [
    target_vertex_colors
]

def get_source(id):
    for source in _sources:
        if source.source_id == id:
            return source

    raise Exception("Source not found: " + id)

def get_target(id):
    for target in _targets:
        if target.target_id == id:
            return target

    raise Exception("Target not found: " + id)

def get_source_enum():
    enumList = []
    i = 0
    for source in _sources:
        enumList.append((source.source_id, source.name, source.description, i))
        i += 1

    return enumList

def get_targets_enum():
    enumList = []
    i = 0
    for target in _targets:
        enumList.append((target.target_id, target.name, target.description, i))
        i += 1

    return enumList
