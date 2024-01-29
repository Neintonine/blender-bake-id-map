import colorsys
import math

import bpy


class BakeToIDMapOperator(bpy.types.Operator):
    bl_idname = "object.bake_to_id_map"
    bl_label = "Bake ID Mask"

    def execute(self, context):

        old_mode = bpy.context.object.mode
        if old_mode != "OBJECT":
            bpy.ops.object.mode_set(mode='OBJECT', toggle=False)

        props = context.scene.bake_to_id_props
        self.paint_id_mask(context, props)

        if old_mode != "OBJECT":
            bpy.ops.object.mode_set(mode=old_mode, toggle=False)

        return {'FINISHED'}

    @staticmethod
    def count_ids(context, props):
        count = 0
        if props.source == 'MATERIAL_INDEX':
            for obj in context.selected_objects:
                count += len(obj.material_slots)

        return count

    def paint_id_mask(self, context, props):
        targets = self.get_targets(context, props)

        if len(targets) < 1:
            return

        totalTargets = len(targets)
        colors = []

        total_hues = props.adv_total_hues
        total_satuations = props.adv_total_satuations
        total_brightnesses = props.adv_total_brightnesses

        satuations_break_point = math.pow(total_brightnesses, total_hues)

        for i in range(totalTargets):
            h = (i / total_hues) % 1
            l = (math.ceil(i / total_hues) % total_brightnesses) / total_brightnesses
            s = math.ceil(i / satuations_break_point) / total_satuations

            colors.append(colorsys.hls_to_rgb(h, l, s))

        self.paint_targets(props, targets, colors)
        self.after_painting(context, props)

    def get_targets(self, context, props):
        if props.source == 'MATERIAL_INDEX':
            return self.get_material_targets(context)

        return []

    def get_material_targets(self, context):
        targets = []
        for obj in context.selected_objects:
            if not obj.material_slots: continue

            mesh = obj.data
            if len(obj.material_slots) < 2:
                targets.append((mesh, mesh.polygons))
                continue

            polygonMaterials = {}
            for poly in mesh.polygons:
                if poly.material_index not in polygonMaterials:
                    polygonMaterials[poly.material_index] = []

                polygonMaterials[poly.material_index].append(poly)

            for polygons in polygonMaterials.values():
                targets.append((mesh, polygons))

        return targets

    def paint_targets(self, props, targets, colors):
        if props.target == 'VERTEX_COLORS':
            self.paint_targets_vertex_colors(props, targets, colors)

    def paint_targets_vertex_colors(self, props, targets, colors):
        sortedTargets = {}
        for i in range(len(targets)):
            target = targets[i]
            obj = target[0]
            indecies = target[1]

            if obj not in sortedTargets:
                sortedTargets[obj] = []

            sortedTargets[obj].append((indecies, colors[i]))

        layer_name = props.target_vertex_color_attribute_name
        for mesh in sortedTargets:
            if layer_name in mesh.vertex_colors:
                mesh.vertex_colors.remove(mesh.vertex_colors[layer_name])

            vertex_color_layer = mesh.vertex_colors.new(name=layer_name)

            for (indecies, color) in sortedTargets[mesh]:
                for polygon in indecies:
                    for idx in polygon.loop_indices:
                        vertex_color_layer.data[idx].color = (color[0], color[1], color[2], 1.0)

    def after_painting(self, context, props):
        if props.source == 'MATERIAL_INDEX':
            self.after_painting_source_material_index(props, context)
            return

    def after_painting_source_material_index(self, props, context):
        if props.source_materials_remove_all:
            for obj in context.selected_objects:
                obj.data.materials.clear()
