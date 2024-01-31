import bpy


class BakeToIDMapPanel(bpy.types.Panel):
    bl_idname = "PANEL.BAKE_TO_ID_MAP_PT_SETTINGS"
    bl_label = "Bake ID Mask"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Tool"

    def draw(self, context):
        layout = self.layout
        layout.use_property_split = True
        layout.use_property_decorate = False  # No animation.

        props = context.scene.bake_to_id_props

        operator_row = layout.row()
        operator_row.operator("object.bake_to_id_map", text="Bake")
        operator_row.enabled = self.check_if_props_valid(context, props)

        layout.prop(props, "selection_mode")

    def check_if_props_valid(self, context, props):
        if (props.selection_mode == "SINGLE" and context.active_object is None):
            return False

        if (props.selection_mode != "SINGLE" and len(context.selected_objects) < 1):
            return False

        return True