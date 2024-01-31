import bpy

from src.properties.id_mask_editor_value_properties import IDMaskEditorValueProperties
from src.types.colors import get_color


class IDEDITOR_CreateIDOperator(bpy.types.Operator):
    bl_idname = "id_mask_editor.create_id_mask"
    bl_label = "id_mask_editor.create_id_mask"

    bl_options = {'INTERNAL'}

    def execute(self, context):
        obj = context.active_object
        if obj.type != 'MESH':
            return {'FINISHED'}

        if not obj.data:
            return {'FINISHED'}

        mesh = obj.data
        properties = mesh.id_mask_editor_properties
        collection = properties.possible_ids
        new_id = collection.add()

        color = get_color(properties.colors)
        colors = color.get_colors(properties)
        colorCount = len(colors)
        current_id_color = colors[properties.current_color_id % colorCount]
        new_id.color = current_id_color
        properties.current_color_id += 1

        return {'FINISHED'}
