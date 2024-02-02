import bpy

class IDEDITOR_SelectIDMaskOperator(bpy.types.Operator):
    bl_idname = "id_mask_editor.select_id_mask"
    bl_label = "Select by ID Mask"
    bl_description = "Selects the faces of the active object, based on current ID mask"

    isCalledFromEditor: bpy.props.BoolProperty(default=False)

    @classmethod
    def poll(cls, context):
        obj = context.active_object
        if obj.type != 'MESH':
            return False

        if not obj.data:
            return False

        mesh = obj.data
        properties = mesh.id_mask_editor_properties

        if not properties.target_attribute:
            return False

        return True

    def execute(self, context):
        obj = context.active_object

        old_mode = bpy.context.object.mode
        if old_mode != "OBJECT":
            bpy.ops.object.mode_set(mode='OBJECT', toggle=False)

        mesh = obj.data
        properties = mesh.id_mask_editor_properties
        color_attribute = mesh.color_attributes.get(properties.target_attribute)

        test_color = self.get_test_color(properties, mesh, color_attribute)
        if not test_color:
            if old_mode != "OBJECT":
                bpy.ops.object.mode_set(mode=old_mode, toggle=False)

            return {'FINISHED'}

        for polygon in mesh.polygons:
            polygon_color = self.get_color_from_polygon(color_attribute, polygon)

            if test_color[0] != polygon_color[0] or test_color[1] != polygon_color[1] or test_color[2] != polygon_color[2]:
                continue

            polygon.select = True

        if old_mode != "OBJECT":
            bpy.ops.object.mode_set(mode=old_mode, toggle=False)

        return {'FINISHED'}

    def get_test_color(self, properties, mesh, color_attribute):
        if self.isCalledFromEditor:
            color = properties.possible_ids[properties.active_id].color
            return (color.r, color.g, color.b, 1.0)

        if mesh.polygons.active:
            return self.get_color_from_polygon(color_attribute, mesh.polygons[mesh.polygons.active])

        return None

    def get_color_from_polygon(self, attribute, polygon):
        color = attribute.data[polygon.loop_indices[0]].color
        return (color[0], color[1], color[2], 1.0)