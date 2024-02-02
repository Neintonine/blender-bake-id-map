import bpy

from .. operators.id_editor_find_used_ids import IDEDITOR_FindUsedIDsOperator


class IDEDITOR_IDMaskEditorOptionsMenu(bpy.types.Menu):
    bl_idname = "VIEW3D_MT_idmask_editor_options"
    bl_label = "Options"

    def draw(self, context):
        layout = self.layout

        layout.operator(IDEDITOR_FindUsedIDsOperator.bl_idname)