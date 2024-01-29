import bpy


class BakeToIDMapPanel(bpy.types.Panel):
    bl_idname = "PANEL.BAKE_TO_ID_MAP_PT_SETTINGS"
    bl_label = "Bake to ID Map"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Tool"

    def draw(self, context):
        layout = self.layout
        layout.use_property_split = True
        layout.use_property_decorate = False  # No animation.

        self.layout.operator("object.bake_to_id_map", text="Bake")
