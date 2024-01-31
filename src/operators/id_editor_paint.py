import bpy

class IDEDITOR_PaintIDMaskOperator(bpy.types.Operator):
    bl_idname = "id_mask_editor.paint_id_mask"
    bl_label = "Paint"
    bl_options = {'INTERNAL'}

    def execute(self, context):
        obj = context.active_object
        if obj.type != 'MESH':
            return {'FINISHED'}

        if not obj.data:
            return {'FINISHED'}

        old_mode = bpy.context.object.mode
        if old_mode != "OBJECT":
            bpy.ops.object.mode_set(mode='OBJECT', toggle=False)

        mesh = obj.data
        properties = mesh.id_mask_editor_properties
        collection = properties.possible_ids
        color = collection[properties.active_id].color

        color_attribute = mesh.color_attributes.get(properties.target_attribute)

        selected_polygons = []
        for polygon in mesh.polygons:
            if not polygon.select:
                continue

            for idx in polygon.loop_indices:
                color_attribute.data[idx].color = (color.r, color.g, color.b, 1.0)

        if old_mode != "OBJECT":
            bpy.ops.object.mode_set(mode=old_mode, toggle=False)

        return {'FINISHED'}
