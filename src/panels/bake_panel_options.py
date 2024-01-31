import textwrap

import bpy

from ..types.colors import get_color
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
        self.draw_options(context, layout, props, source)

        layout.separator()

        layout.prop(props, "target")
        target = get_target(props.target)
        self.draw_options(context, layout, props, target)

        layout.separator()

        layout.prop(props, "colors")
        color = get_color(props.colors)
        self.draw_options(context, layout, props, color)

    def draw_options(self, context, layout, props, element):

        has_render_ui = 'render_ui' in dir(element)
        has_connected_properties = 'connected_properties' in dir(element) and len(element.connected_properties) > 0

        if not has_render_ui and not has_connected_properties:
            return

        object_box = layout.box()

        if has_render_ui:
            element.render_ui(context, object_box, props)
            return

        for setting in element.connected_properties:
            object_box.prop(props, setting)