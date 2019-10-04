import bpy, bmesh, math
from blender2nier.util import *
from blender2nier.generate_data import *
from blender2nier.wmb.wmb_header import *
from blender2nier.wmb.wmb_bones import *
from blender2nier.wmb.wmb_boneIndexTranslateTable import *
from blender2nier.wmb.wmb_vertexGroups import *
from blender2nier.wmb.wmb_batches import *
from blender2nier.wmb.wmb_lods import *
from blender2nier.wmb.wmb_meshMaterials import *
from blender2nier.wmb.wmb_boneMap import *
from blender2nier.wmb.wmb_meshes import *
from blender2nier.wmb.wmb_materials import *

def reset_blend():
    print('Preparing .blend File:')
    for obj in bpy.data.objects:
        if obj.type not in ['MESH', 'ARMATURE']:
            print('[-] Removing ', obj)
            bpy.data.objects.remove(obj)

def main(filepath):
    reset_blend()

    wmb_file = create_wmb(filepath)

    generated_data = c_generate_data()

    create_wmb_header(wmb_file, generated_data)

    create_wmb_bones(wmb_file, generated_data)

    create_wmb_boneIndexTranslateTable(wmb_file, generated_data)

    create_wmb_vertexGroups(wmb_file, generated_data)

    create_wmb_batches(wmb_file, generated_data)
    
    create_wmb_lods(wmb_file, generated_data)

    create_wmb_meshMaterials(wmb_file, generated_data)

    create_wmb_boneMap(wmb_file, generated_data)

    create_wmb_meshes(wmb_file, generated_data)

    create_wmb_materials(wmb_file, generated_data)

    close_wmb(wmb_file)
    return {'FINISHED'}