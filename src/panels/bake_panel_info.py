import bpy

from ..types.colors import get_color
from .. types.sources import get_source


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

        if props.selection_mode != 'SINGLE':
            layout.label(text="Selected Object-Count: " + str(len(context.selected_objects)))

        if props.selection_mode == 'SINGLE':
            layout.label(text="ID-Total: " + str(source.estimate_ids([context.active_object])))

        if props.selection_mode == 'MULTIPLE_SEPARATE':
            total = 0
            count = 0
            for obj in context.selected_objects:
                if (obj.type != 'MESH'):
                    continue

                total += source.estimate_ids([obj])
                count += 1

            layout.label(text="Estimated ID-Total: " + str(total))
            try:
                layout.label(text="Estimated ID-Average: " + str(total / count))
            except ZeroDivisionError:
                layout.label(text="Estimated ID-Average: 0")

        if props.selection_mode == 'MULTIPLE_COMBINED':
            layout.label(text="ID-Total: " + str(source.estimate_ids(context.selected_objects)))

        color = get_color(props.colors)

        layout.label(text="Colors available: " + str(color.get_count(props)))
