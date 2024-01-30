import colorsys
import math

import bpy

from .. types import (get_source, get_target)


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

    def paint_id_mask(self, context, props):
        source = get_source(props.source)

        targets = self.get_targets(context, source, props)

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

        target = get_target(props.target)
        self.paint_targets(props, target, targets, colors)
        if 'after_painting' in dir(source):
            source.after_painting(context, props)

    def get_targets(self, context, source, props):
        if props.selection_mode == 'SINGLE':
            return source.get_targets([context.active_object])

        if props.selection_mode == 'MULTIPLE_COMBINED':
            return source.get_targets(context.selected_objects)

        if props.selection_mode == 'MULTIPLE_SEPARATE':
            result = []
            for obj in context.selected_objects:
                if obj.type != 'MESH':
                    continue

                obj_targets = source.get_targets([obj])
                result.append(obj_targets)

            return result

        raise ValueError('Invalid selection_mode')

    def paint_targets(self, props, target, targets, colors):
        if props.selection_mode == 'MULTIPLE_SEPARATE':
            for targetList in targets:
                target.paint_targets(props,targetList, colors)

            return

        target.paint_targets(props, targets, colors)