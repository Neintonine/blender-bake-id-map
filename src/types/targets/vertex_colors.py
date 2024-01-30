target_id = 'VERTEX_COLORS'
name = 'Vertex Colors'
description = 'Bakes the ID onto the vertex color'

connected_properties = [
    'target_vertex_color_attribute_name'
]


def paint_targets(props, targets, colors):
    sortedTargets = {}
    for i in range(len(targets)):
        target = targets[i]
        obj = target[0]
        indecies = target[1]

        if obj not in sortedTargets:
            sortedTargets[obj] = []

        sortedTargets[obj].append((indecies, colors[i]))

    layer_name = props.target_vertex_color_attribute_name
    for mesh in sortedTargets:
        if layer_name in mesh.vertex_colors:
            mesh.vertex_colors.remove(mesh.vertex_colors[layer_name])

        vertex_color_layer = mesh.vertex_colors.new(name=layer_name)

        for (indecies, color) in sortedTargets[mesh]:
            for polygon in indecies:
                for idx in polygon.loop_indices:
                    vertex_color_layer.data[idx].color = (color[0], color[1], color[2], 1.0)