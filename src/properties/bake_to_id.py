from bpy.types import (PropertyGroup)
from bpy.props import (EnumProperty, BoolProperty, IntProperty, StringProperty)

from src.types import get_source_enum, get_targets_enum


class BakeToIDProperties(PropertyGroup):
    selection_mode: EnumProperty(
        items=[
            ("SINGLE", "Only active element", "Only use the currently selected element", 0),
            ("MULTIPLE_SEPARATE", "Use Selection, separate", "It performs the transfer for every selected element, but each get there own ids", 1),
            ("MULTIPLE_COMBINED", "Use Selection, combined", "It performs the transfer for every selected element, combining the ids", 2)
        ],
        name="Selection Mode",
        description="Specifies how the 3D View-Selection is gonna be used.",
        default="MULTIPLE_SEPARATE"
    )

    source: EnumProperty(
        items=get_source_enum(),
        name="Source",
        description="From where should the IDs be taken",
        default="MATERIAL_INDEX"

    )
    target: EnumProperty(
        items=get_targets_enum(),
        name="Target",
        description="To where should the IDs should be baked to",
        default=get_targets_enum()[0][0]
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
    target_vertex_color_override_attribute: BoolProperty(
        name="Override Color Attribute",
        default=True,
        description="If set true, the attribute will be deleted and recreated, if it already exists. If set false, the data will just be overwritten."
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