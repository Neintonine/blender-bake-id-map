source_id = 'MATERIAL_INDEX'
name = 'Material Index'
description = 'Uses the current material index as basis for ID mask.'

connected_properties = [
    'source_materials_remove_all'
]

def get_targets(objects):
    targets = []
    for obj in objects:
        if not obj.material_slots: continue

        mesh = obj.data
        if len(obj.material_slots) < 2:
            targets.append((mesh, mesh.polygons))
            continue

        polygonMaterials = {}
        for poly in mesh.polygons:
            if poly.material_index not in polygonMaterials:
                polygonMaterials[poly.material_index] = []

            polygonMaterials[poly.material_index].append(poly)

        for polygons in polygonMaterials.values():
            targets.append((mesh, polygons))

    return targets

def after_painting(context, props):
    if props.source_materials_remove_all:
        for obj in context.selected_objects:
            obj.data.materials.clear()

def estimate_ids(objects):
    count = 0
    for obj in objects:
        count += len(obj.material_slots)

    return count
