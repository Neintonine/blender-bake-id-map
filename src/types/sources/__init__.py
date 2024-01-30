from . import material_index
from . import object

_sources = [
    material_index,
    object
]

def get_source(id):
    for source in _sources:
        if source.source_id == id:
            return source

    raise Exception("Source not found: " + id)


def get_source_enum():
    enum_list = []
    i = 0
    for source in _sources:
        enum_list.append((source.source_id, source.name, source.description, i))
        i += 1

    return enum_list

