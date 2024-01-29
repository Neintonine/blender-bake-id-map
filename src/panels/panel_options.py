import bpy


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
        source_settings_box = layout.box()
        source_settings = self.get_source_settings(props)
        for setting in source_settings:
            source_settings_box.prop(props, setting)

        layout.separator()

        layout.prop(props, "target")
        target_settings_box = layout.box()
        target_settings = self.get_target_settings(props)
        for setting in target_settings:
            target_settings_box.prop(props, setting)

    def get_source_settings(self, props):
        if props.source == 'MATERIAL_INDEX':
            return [
                'source_materials_remove_all'
            ]

        return []

    def get_target_settings(self, props):
        if props.target == 'VERTEX_COLORS':
            return [
                'target_vertex_color_attribute_name'
            ]

        return []