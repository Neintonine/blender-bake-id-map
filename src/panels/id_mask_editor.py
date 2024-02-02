import bpy

from .. menu.id_mask_editor_options import IDEDITOR_IDMaskEditorOptionsMenu
from .. operators.create_id_mask import CreateIDMaskOperator
from .. operators.id_editor_apply_color import IDEDITOR_ColorApplyOperator
from .. operators.id_editor_create_id import IDEDITOR_CreateIDOperator
from .. operators.id_editor_paint import IDEDITOR_PaintIDMaskOperator
from .. operators.id_editor_remove_id import IDEDITOR_RemoveIDOperator
from .. operators.id_editor_revert_color import IDEDITOR_ColorResetOperator
from .. operators.id_mask_select import IDEDITOR_SelectIDMaskOperator
from .. types.colors import get_color


class IDMaskEditorPanel(bpy.types.Panel):
    bl_idname = "ID_MASK_EDITOR_PT_Panel"
    bl_label = "ID Mask Editor"
    bl_category = "Tool"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    @classmethod
    def poll(cls, context):
        if not context.object:
            return False

        if not context.object.type == 'MESH':
            return False

        return context.object.mode == "EDIT"

    def draw(self, context):
        layout = self.layout
        layout.use_property_decorate = True

        mesh = context.object.data
        properties = mesh.id_mask_editor_properties

        target_attribute_row = layout.row(align=True)
        has_attribute = properties.target_attribute

        target_attribute_row.prop_search(
            properties,
            'target_attribute',
            mesh,
            'color_attributes',
            icon='GROUP_VCOL'
        )
        target_attribute_row.operator(CreateIDMaskOperator.bl_idname, icon='ADD', text="")

        if not has_attribute:
            return

        layout.prop(properties, "colors")
        color = get_color(properties.colors)
        self.draw_options(context, layout, properties, color)

        layout.separator()

        row = layout.row()

        col = row.column()

        col.template_list(
            'IDMaskEditorIDList',
            'IDMaskEditorIDList',
            properties,
            'possible_ids',
            properties,
            'active_id',
            rows=3
        )

        button_row = col.row()
        button_row.operator(IDEDITOR_PaintIDMaskOperator.bl_idname, text='Paint', icon='VPAINT_HLT')
        button_row.operator(IDEDITOR_SelectIDMaskOperator.bl_idname, text='Select', icon='SELECT_SET').isCalledFromEditor = True

        color_button_row = button_row.row(align=True)
        has_color_changed = False
        for id in properties.possible_ids:
            if not id.color_changed:
                continue
            has_color_changed = True
            break

        color_button_row.enabled = has_color_changed

        reset_op = color_button_row.operator(IDEDITOR_ColorResetOperator.bl_idname, icon='LOOP_BACK', text='Reset Colors')
        reset_op.triggeredByList = False

        apply_op = color_button_row.operator(IDEDITOR_ColorApplyOperator.bl_idname, icon='CHECKMARK', text='Apply Colors')
        apply_op.triggeredByList = False


        col = row.column(align=True)
        col.operator(IDEDITOR_CreateIDOperator.bl_idname, icon='ADD', text="")
        col.operator(IDEDITOR_RemoveIDOperator.bl_idname, icon='REMOVE', text="")
        col.separator()

        col.menu(IDEDITOR_IDMaskEditorOptionsMenu.bl_idname, icon='DOWNARROW_HLT', text="")


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