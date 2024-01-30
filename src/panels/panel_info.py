import bpy

from .. operators.bake_to_id_map import BakeToIDMapOperator
from ..types import get_source


class BakeToIDInfoPanel(bpy.types.Panel):
    bl_idname = "PANEL.BAKE_TO_ID_MAP_PT_SETTINGS_INFO"
    bl_parent_id = "PANEL.BAKE_TO_ID_MAP_PT_SETTINGS"
    bl_label = "Infos"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Tool"

    def draw(self, context):
        layout = self.layout

        props = context.scene.bake_to_id_props

        source = get_source(props.source)

        layout.label(text="Selected Object-Count: " + str(len(context.selected_objects)))
        layout.label(text="Estimated ID-Count: " + str(source.estimate_ids(context, props)))