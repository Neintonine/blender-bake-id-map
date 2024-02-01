import bpy

from src.operators.id_mask_select import IDEDITOR_SelectIDMaskOperator

def id_mask_select_menu_function(self, context):
    self.layout.operator(IDEDITOR_SelectIDMaskOperator.bl_idname).isCalledFromEditor = False

def register():
    bpy.types.VIEW3D_MT_select_edit_mesh.append(id_mask_select_menu_function)

def unregister():
    bpy.types.VIEW3D_MT_select_edit_mesh.remove(id_mask_select_menu_function)