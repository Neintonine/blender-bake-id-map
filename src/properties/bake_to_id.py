from bpy.types import (PropertyGroup)
from bpy.props import (EnumProperty, BoolProperty, IntProperty, StringProperty)

from src.types import get_source_enum, get_targets_enum


class BakeToIDProperties(PropertyGroup):
    source: EnumProperty(
        items=get_source_enum(),
        name="Source",
        description="From where should the IDs be taken",
        default = "MATERIAL_INDEX"

    )
    target: EnumProperty(
        items=get_targets_enum(),
        name="Target",
        description="To where should the IDs should be baked to",
        default="VERTEX_COLORS"
    )

    source_materials_remove_all : BoolProperty(
        name="Remove all source materials",
        default=False,
        description="Removes every material except the first one."
    )

    target_vertex_color_attribute_name: StringProperty(
        name="Color Attribute",
        default="ID_MASK",
    )

    adv_total_hues: IntProperty(
        name="Total Hues",
        default=10,
        min=1,
        soft_max=360,
    )

    adv_total_satuations: IntProperty(
        name="Total Satuations",
        default=10,
        min=1,
        soft_max=100,
    )

    adv_total_brightnesses: IntProperty(
        name="Total Brightnesses",
        default=10,
        min=1,
        soft_max=100,
    )