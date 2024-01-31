from bpy.types import (PropertyGroup)
from bpy.props import (StringProperty, FloatVectorProperty)

class IDMaskEditorValueProperties(PropertyGroup):
    name: StringProperty(
        name="Name",
        description="ID-Name",
        default='ID'
    )

    color: FloatVectorProperty(
        name="Color",
        subtype='COLOR',
        default=[1.0, 1.0, 1.0],
        min=0,
        max=1
    )