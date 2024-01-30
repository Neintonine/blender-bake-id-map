source_id = 'OBJECT'
name = 'Object ID'
description = 'Uses the object id as basis for the ID mask.'

connected_properties = []

def get_targets(context):
    targets = []
    for obj in context.selected_objects:
        mesh = obj.data
        targets.append((mesh, mesh.polygons))

    return targets

def estimate_ids(context, props):
    return len(context.selected_objects)