bl_info = {
    "name": "Bake ID Mask",
    "author": "iedSoftworks",
    "description": "",
    # !VERSION
    "blender": (2, 92, 0),
    "category": "Object"
}

import bpy

from . panels.panel_options import BakeToIDOptionsPanel
from . panels.panel_advanced import BakeToIDAdvancedMenu
from . operators.bake_to_id_map import BakeToIDMapOperator
from . panels.panel import BakeToIDMapPanel
from . panels.panel_info import BakeToIDInfoPanel
from . properties.bake_to_id import BakeToIDProperties

classes = (
    BakeToIDMapOperator,
    BakeToIDMapPanel,
    BakeToIDInfoPanel,
    BakeToIDOptionsPanel,
    BakeToIDAdvancedMenu,
    BakeToIDProperties,
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    setattr(bpy.types.Scene, 'bake_to_id_props', bpy.props.PointerProperty(type=BakeToIDProperties))


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)

    del bpy.types.Scene.bake_to_id_props


if __name__ == "__main__":
    register()
