target_id = 'COLOR_ATTRIBUTE'
name = 'Color Attribute / Vertex Color'
description = 'Bakes the ID onto a color attribute (previously known as Vertex Color)'

connected_properties = [
    'target_vertex_color_attribute_name',
    'target_vertex_color_override_attribute'
]


def paint_targets(props, targets, colors):
    sorted_targets = {}
    colors_amount = len(colors)
    for i in range(len(targets)):
        target = targets[i]
        obj = target[0]
        indecies = target[1]

        if obj not in sorted_targets:
            sorted_targets[obj] = []

        sorted_targets[obj].append((indecies, colors[i % colors_amount]))

    layer_name = props.target_vertex_color_attribute_name
    for mesh in sorted_targets:

        if layer_name in mesh.attributes:
            mesh.attributes.remove(mesh.attributes[layer_name])

        color_attribute = get_color_attribute(props, mesh.attributes, layer_name)

        for (indecies, color) in sorted_targets[mesh]:
            for polygon in indecies:
                for idx in polygon.loop_indices:
                    color_attribute.data[idx].color = (color[0], color[1], color[2], 1.0)

def get_color_attribute(props, attributes, layer_name):
    if layer_name in attributes:
        if not props.target_vertex_color_override_attribute:
            return attributes[layer_name]

        attributes.remove(attributes[layer_name])

    return attributes.new(name=layer_name, type='FLOAT_COLOR', domain='CORNER')