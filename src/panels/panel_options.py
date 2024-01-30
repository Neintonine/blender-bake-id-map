import textwrap

import bpy

from .. types.sources import get_source
from .. types.targets import get_target


class BakeToIDOptionsPanel(bpy.types.Panel):
    bl_idname = "PANEL.BAKE_TO_ID_MAP_PT_SETTINGS_OPTIONS"
    bl_parent_id = "PANEL.BAKE_TO_ID_MAP_PT_SETTINGS"
    bl_label = "Options"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Tool"

    def draw(self, context):
        layout = self.layout
        layout.use_property_split = True
        layout.use_property_decorate = False  # No animation.

        props = context.scene.bake_to_id_props

        layout.prop(props, "source")
        source = get_source(props.source)

        if len(source.connected_properties) > 0:
            source_settings_box = layout.box()
            for setting in source.connected_properties:
                source_settings_box.prop(props, setting)

        layout.separator()

        layout.prop(props, "target")
        target = get_target(props.target)
        if len(target.connected_properties) > 0:
            target_settings_box = layout.box()
            for setting in target.connected_properties:
                target_settings_box.prop(props, setting)

        layout.separator()

        layout.prop(props, "colors")
