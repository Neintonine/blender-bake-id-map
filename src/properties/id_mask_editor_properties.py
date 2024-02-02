import bpy

from bpy.types import (PropertyGroup, Palette, FloatColorAttribute)
from bpy.props import (EnumProperty, BoolProperty, IntProperty, StringProperty, PointerProperty, CollectionProperty)

from .. properties.id_mask_editor_value_properties import IDMaskEditorValueProperties
from .. types.colors import get_color_enum

def on_target_attribute_set(self, value):
    return None

def on_target_attribute_get(self):
    if bpy.context.active_object is None:
        return None

    if bpy.context.active_object.data is None:
        return None

    if bpy.context.active_object.type != 'MESH':
        return None

    color_attributes = bpy.context.active_object.data.color_attributes[0]

    return color_attributes

class IDMaskEditorProperties(PropertyGroup):
    colors: EnumProperty(
        items=get_color_enum(),
        name="Color Source",
        description="From where to take the colors",
        default=get_color_enum()[0][0]
    )

    colors_color_palette_palette: PointerProperty(
        type=Palette,
        name='Color Palette',
        description="The Color Palette used for colors"
    )

    target_attribute: StringProperty(
        name='',
        description="The attribute to write the ID Mask to"
    )

    possible_ids: CollectionProperty(
        type=IDMaskEditorValueProperties,
        name='Entries',
    )

    active_id: IntProperty(
        name="",
        description="",
        default=0
    )

    current_color_id: IntProperty(
        default=0
    )