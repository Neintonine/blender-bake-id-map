import bpy

class IDEDITOR_FindUsedIDsOperator(bpy.types.Operator):
    bl_idname = "id_mask_editor.find_used_ids"
    bl_label = "Find used colors"
    bl_description = "Searches the current ID-mask for colors and adds them to the id-list"

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
        for color_data in color_attribute.data:
            colors.append((color_data.color[0], color_data.color[1], color_data.color[2]))

        i = 0
        set_colors = set(colors)
        for color in set_colors:
            has_color = False
            for color_id in properties.possible_ids:
                has_color = (color_id.color.r == color[0] and
                             color_id.color.g == color[1] and
                             color_id.color.b == color[2])

                if has_color:
                    break

            if has_color:
                continue

            color_identifier = properties.possible_ids.add()
            color_identifier.color = (color[0], color[1], color[2])
            color_identifier.name = "Imported ID " + str(i + 1)
            i += 1

        if old_mode != "OBJECT":
            bpy.ops.object.mode_set(mode=old_mode, toggle=False)

        return {'FINISHED'}