import bpy

from . menu import id_mask_select_menu
from . menu.id_mask_editor_options import IDEDITOR_IDMaskEditorOptionsMenu
from . operators.create_id_mask import CreateIDMaskOperator
from . operators.id_editor_apply_color import IDEDITOR_ColorApplyOperator
from . operators.id_editor_create_id import IDEDITOR_CreateIDOperator
from . operators.id_editor_find_used_ids import IDEDITOR_FindUsedIDsOperator
from . operators.id_editor_paint import IDEDITOR_PaintIDMaskOperator
from . operators.id_editor_remove_id import IDEDITOR_RemoveIDOperator
from . operators.id_editor_revert_color import IDEDITOR_ColorResetOperator
from . operators.id_mask_select import IDEDITOR_SelectIDMaskOperator
from . panels.id_mask_editor_id_list import IDMaskEditorIDList
from . properties.id_mask_editor_value_properties import IDMaskEditorValueProperties
from . panels.bake_panel_options import BakeToIDOptionsPanel
from . operators.bake_to_id_map import BakeToIDMapOperator
from . panels.bake_panel import BakeToIDMapPanel
from . panels.bake_panel_info import BakeToIDInfoPanel
from . panels.id_mask_editor import IDMaskEditorPanel
from . properties.bake_properties import BakeToIDProperties

from . properties.id_mask_editor_properties import IDMaskEditorProperties

bl_info = {
    "name": "ID Mask - Tools",
    "author": "iedSoftworks",
    "description": "",
    # !VERSION
    "blender": (2, 92, 0),
    "category": "Object"
}

classes = (
    BakeToIDMapOperator,
    BakeToIDMapPanel,
    BakeToIDInfoPanel,
    BakeToIDOptionsPanel,
    BakeToIDProperties,

    IDMaskEditorValueProperties,
    IDMaskEditorProperties,
    IDMaskEditorPanel,
    CreateIDMaskOperator,
    IDMaskEditorIDList,
    IDEDITOR_CreateIDOperator,
    IDEDITOR_RemoveIDOperator,
    IDEDITOR_PaintIDMaskOperator,
    IDEDITOR_SelectIDMaskOperator,
    IDEDITOR_FindUsedIDsOperator,
    IDEDITOR_IDMaskEditorOptionsMenu,
    IDEDITOR_ColorResetOperator,
    IDEDITOR_ColorApplyOperator,
)

menu_additions = [
    id_mask_select_menu
]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    for menu in menu_additions:
        menu.register()

    setattr(bpy.types.Scene, 'bake_to_id_props', bpy.props.PointerProperty(type=BakeToIDProperties))
    setattr(bpy.types.Mesh, 'id_mask_editor_properties', bpy.props.PointerProperty(type=IDMaskEditorProperties))

def unregister():
    for menu in reversed(menu_additions):
        menu.unregister()

    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)


    del bpy.types.Scene.bake_to_id_props


if __name__ == "__main__":
    register()
