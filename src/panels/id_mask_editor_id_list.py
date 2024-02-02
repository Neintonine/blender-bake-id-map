import bpy

from .. operators.id_editor_apply_color import IDEDITOR_ColorApplyOperator
from .. operators.id_editor_revert_color import IDEDITOR_ColorResetOperator


class IDMaskEditorIDList(bpy.types.UIList):
    def draw_item(self, _context, layout, data, attribute, _icon, _active_data, _active_propname, _index):
        layout.alignment = 'EXPAND'

        split = layout.split(factor=0.15)
        split.alignment = 'LEFT'
        split.prop(attribute, 'color', text='')

        row = split.row()
        col = row.column()
        col.alignment = 'RIGHT'
        col.emboss = 'NONE'
        col.prop(attribute, "name", text="")
        col.emboss = 'NORMAL'

        row1 = row.row(align=True)
        row1.enabled = attribute.color_changed
        reset_op = row1.operator(IDEDITOR_ColorResetOperator.bl_idname, icon='LOOP_BACK', text='')
        reset_op.triggeredByList = True
        reset_op.listId = _index

        apply_op = row1.operator(IDEDITOR_ColorApplyOperator.bl_idname, icon='CHECKMARK', text='')
        apply_op.triggeredByList = True
        apply_op.listId = _index
