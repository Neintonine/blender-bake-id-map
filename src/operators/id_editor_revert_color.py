import bpy

class IDEDITOR_ColorResetOperator(bpy.types.Operator):
    bl_idname = "id_mask_editor.reset_colors"
    bl_label = "Resets ID-Mask colors"
    bl_description = "Resets the colors to the previous values"
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

        mesh = obj.data
        properties = mesh.id_mask_editor_properties

        if self.triggeredByList:
            self.reset_color(properties.possible_ids[self.listId])
            return {'FINISHED'}

        for prop in properties.possible_ids:
            self.reset_color(prop)

        return {'FINISHED'}

    def reset_color(self, value):
        if not value.color_changed:
            return

        value.color = value.original_color
        value.color_changed = False
