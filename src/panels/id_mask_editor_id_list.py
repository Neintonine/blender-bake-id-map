import bpy

from src.operators.id_editor_paint import IDEDITOR_PaintIDMaskOperator


class IDMaskEditorIDList(bpy.types.UIList):
    def draw_item(self, _context, layout, data, attribute, _icon, _active_data, _active_propname, _index):
        layout.alignment = 'EXPAND'

        split = layout.split(factor=0.15)
        split.alignment = 'LEFT'
        split.prop(attribute, 'color', text='')

        split.emboss = 'NONE'
        split2 = split.split(factor=0.75)
        split2.prop(attribute, "name", text="")
        split2.emboss = 'NORMAL'