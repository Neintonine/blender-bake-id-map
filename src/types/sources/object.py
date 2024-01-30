source_id = 'OBJECT'
name = 'Object ID'
description = 'Uses the object id as basis for the ID mask.'

connected_properties = []

def get_targets(objects):
    targets = []
    for obj in objects:
        mesh = obj.data
        targets.append((mesh, mesh.polygons))

    return targets

def estimate_ids(objects):
    return len(objects)