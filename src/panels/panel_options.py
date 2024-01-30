import textwrap

import bpy

from src.types import get_source, get_target


class BakeToIDOptionsPanel(bpy.types.Panel):
    bl_idname = "PANEL.BAKE_TO_ID_MAP_PT_SETTINGS_OPTIONS"
    bl_parent_id = "PANEL.BAKE_TO_ID_MAP_PT_SETTINGS"
    bl_label = "Options"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Tool"

    def draw(self, context):
        layout = self.layout

        props = context.scene.bake_to_id_props

        layout.prop(props, "source")
        source = get_source(props.source)
        source_settings_box = layout.box()
        for setting in source.connected_properties:
            source_settings_box.prop(props, setting)

        layout.separator()

        layout.prop(props, "target")
        target = get_target(props.target)
        target_settings_box = layout.box()
        for setting in target.connected_properties:
            target_settings_box.prop(props, setting)
