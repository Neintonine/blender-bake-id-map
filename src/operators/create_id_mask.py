import bpy


class CreateIDMaskOperator(bpy.types.Operator):
    bl_idname = "id_mask_editor.create_id_mask_attribute"
    bl_label = "Create ID Mask - Attribute"
    bl_options = {'INTERNAL'}

    @classmethod
    def poll(cls, context):

        obj = context.active_object
        if obj.type != 'MESH':
            return False

        if not obj.data:
            return False

        mesh = obj.data
        return 'ID_MASK' not in mesh.color_attributes

    def execute(self, context):
        obj = context.active_object
        if obj.type != 'MESH':
            return {'FINISHED'}

        if not obj.data:
            return {'FINISHED'}

        mesh = obj.data

        if 'ID_MASK' in mesh.color_attributes:
            return {'FINISHED'}

        bpy.ops.geometry.color_attribute_add(name='ID_MASK', data_type='FLOAT_COLOR', domain='CORNER')
        mesh.id_mask_editor_properties.target_attribute = 'ID_MASK'

        return {'FINISHED'}
