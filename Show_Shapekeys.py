import bpy
from bpy.types import Panel
from bpy.props import *



class fake_context:
    def __init__(self): 
        self.object = None

class SHK_PT_panel(Panel):
    bl_label = "Shape Keys"
    bl_id = "SHK_PT_panel"
    
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Shape Keys"
    
    
    def draw(self,context):
        scene = context.scene
        layout = self.layout
        _context = fake_context
        _context.object = context.scene.sk_object
        layout.prop(scene,'sk_collection')
        layout.prop(scene,'sk_object')
        if context.scene.sk_object:
            bpy.types.DATA_PT_shape_keys.draw(self,_context)
        
def object_poll(self,object):
    
    return object.name in bpy.context.scene.sk_collection.objects and object.type == 'MESH' and object.data.shape_keys
    
        
def register():
    bpy.utils.register_class(SHK_PT_panel)
    bpy.types.Scene.sk_object = PointerProperty(name = 'Mesh',type= bpy.types.Object,poll = object_poll)
    bpy.types.Scene.sk_collection = PointerProperty(name = 'Collection',type=bpy.types.Collection)


def unregister():
    bpy.utils.unregister_class(SHK_PT_panel)


if __name__ == "__main__":
    register()

     
    
