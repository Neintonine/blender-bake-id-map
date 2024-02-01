import bpy

class IDEDITOR_ColorApplyOperator(bpy.types.Operator):
    bl_idname = "id_mask_editor.apply_colors"
    bl_label = "Apply changed ID-Mask colors"
    bl_description = "Searches the current ID-mask for colors and adds them to the id-list"
    bl_options = {'INTERNAL'}

    triggeredByList: bpy.props.BoolProperty(default=False)
    listId: bpy.props.IntProperty(default=0)

    @classmethod
    def poll(cls, context):
        obj = context.active_object
        if obj.type != 'MESH':
            return False

        if not obj.data:
            return False

        mesh = obj.data
        properties = mesh.id_mask_editor_properties

        if not properties.target_attribute:
            return False

        return True

    def execute(self, context):
        obj = context.active_object

        old_mode = bpy.context.object.mode
        if old_mode != "OBJECT":
            bpy.ops.object.mode_set(mode='OBJECT', toggle=False)
        mesh = obj.data
        properties = mesh.id_mask_editor_properties
        color_attribute = mesh.color_attributes.get(properties.target_attribute)

        colors = []

        if self.triggeredByList:
            list_item = properties.possible_ids[self.listId]
            if list_item.color_changed:
                colors.append((list_item.original_color, list_item.color))
        else:
            for id in properties.possible_ids:
                if not id.color_changed:
                    continue

                colors.append((id.original_color, id.color))

        for polygon in mesh.polygons:
            polygon_color = self.get_color_from_polygon(color_attribute, polygon)

            for (original_color, color) in colors:
                if original_color[0] != polygon_color[0] or original_color[1] != polygon_color[1] or original_color[2] != polygon_color[2]:
                    continue

                for idx in polygon.loop_indices:
                    color_attribute.data[idx].color = (color.r, color.g, color.b, 1.0)

                break

        if self.triggeredByList:
            list_item = properties.possible_ids[self.listId]
            list_item.color_changed = False
        else:
            for id in properties.possible_ids:
                id.color_changed = False

        if old_mode != "OBJECT":
            bpy.ops.object.mode_set(mode=old_mode, toggle=False)
        return {'FINISHED'}

    def reset_color(self, value):
        if not value.color_changed:
            return

        value.color = value.original_color
        value.color_changed = False

    def get_color_from_polygon(self, attribute, polygon):
        color = attribute.data[polygon.loop_indices[0]].color
        return (color[0], color[1], color[2], 1.0)