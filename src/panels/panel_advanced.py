import math

import bpy


class BakeToIDAdvancedMenu(bpy.types.Panel):
    bl_idname = "PANEL.BAKE_TO_ID_MAP_PT_SETTINGS_ADVANCED"
    bl_parent_id = "PANEL.BAKE_TO_ID_MAP_PT_SETTINGS"
    bl_label = "Advanced"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Tool"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout

        props = context.scene.bake_to_id_props
        layout.label(text="Colors")
        layout.prop(props, "adv_total_hues")
        layout.prop(props, "adv_total_satuations")
        layout.prop(props, "adv_total_brightnesses")
        layout.label(text="Max ID-count: " + str(
            ))
