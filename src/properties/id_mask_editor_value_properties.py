from bpy.types import (PropertyGroup)
from bpy.props import (StringProperty,BoolProperty, FloatVectorProperty)

def get_color(self):
    return self['color']

def set_color(self, value):
    if 'color' not in self:
        self['color'] = value
        return

    prev_color = self['color']

    if not self.color_changed:
        self.color_changed = True
        self.original_color = prev_color

    self['color'] = value

class IDMaskEditorValueProperties(PropertyGroup):
    name: StringProperty(
        name="Name",
        description="ID-Name",
        default='ID'
    )

    color_changed: BoolProperty(
        default=False
    )

    color: FloatVectorProperty(
        name="Color",
        subtype='COLOR',
        default=[1.0, 1.0, 1.0],
        min=0,
        max=1,
        get=get_color,
        set=set_color
    )

    original_color: FloatVectorProperty(
        name="Original Color",
        subtype='COLOR',
        default=[1.0, 1.0, 1.0],
        min=0,
        max=1
    )