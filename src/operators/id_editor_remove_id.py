import bpy

class IDEDITOR_RemoveIDOperator(bpy.types.Operator):
    bl_idname = "id_mask_editor.remove_id_mask"
    bl_label = "id_mask_editor.remove_id_mask"

    bl_options = {'INTERNAL'}

    @classmethod
    def poll(cls, context):

        obj = context.active_object
        if obj.type != 'MESH':
            return False

        if not obj.data:
            return False

        mesh = obj.data
        properties = mesh.id_mask_editor_properties
        collection = properties.possible_ids
        return 0 <= properties.active_id < len(collection)

    def execute(self, context):
        obj = context.active_object
        if obj.type != 'MESH':
            return {'FINISHED'}

        if not obj.data:
            return {'FINISHED'}

        mesh = obj.data
        properties = mesh.id_mask_editor_properties
        collection = properties.possible_ids
        collection.remove(properties.active_id)

        return {'FINISHED'}
