bl_info = {
    "name": "Add Human Metarig",
    "author": "Christopher S. Francis",
    "version": (1, 1),
    "blender": (3, 5, 0),
    "location": "run script",
    "description": "Adds a scaled and rotated rigify basic human metarig",
    "warning": "",
    "wiki_url": "",
    "category": "Add Armature",
}


import bpy
import addon_utils


load_default, load_state = addon_utils.check("rigify")
if not load_state:
    addon_utils.enable("rigify")


bpy.ops.object.armature_basic_human_metarig_add()
bpy.ops.transform.resize(value=(0.90, 0.90, 0.90))



bpy.ops.object.posemode_toggle()
for obj in bpy.data.objects["metarig"].pose.bones:
    obj.bone.select = False

##arms
bpy.data.objects['metarig'].pose.bones["upper_arm.R"].bone.select = True
bpy.ops.transform.rotate(value=0.667, orient_axis='Y')
bpy.ops.transform.rotate(value=0.172, orient_axis='X')
bpy.data.objects['metarig'].pose.bones["upper_arm.R"].bone.select = False

bpy.data.objects['metarig'].pose.bones["upper_arm.L"].bone.select = True
bpy.ops.transform.rotate(value=-0.667, orient_axis='Y')
bpy.ops.transform.rotate(value=0.172, orient_axis='X')
bpy.data.objects['metarig'].pose.bones["upper_arm.L"].bone.select = False


#legs
bpy.data.objects['metarig'].pose.bones["thigh.R"].bone.select = True
bpy.ops.transform.rotate(value=-0.0404, orient_axis='Y')
bpy.ops.transform.rotate(value=-0.0446, orient_axis='X')
bpy.data.objects['metarig'].pose.bones["thigh.R"].bone.select = False

bpy.data.objects['metarig'].pose.bones["thigh.L"].bone.select = True
bpy.ops.transform.rotate(value=0.0527, orient_axis='Y')
bpy.ops.transform.rotate(value=-0.0567, orient_axis='X')
bpy.data.objects['metarig'].pose.bones["thigh.L"].bone.select = False



for obj in bpy.data.objects["metarig"].pose.bones:
    obj.bone.select = True
bpy.ops.pose.armature_apply(selected=True)


bpy.ops.object.posemode_toggle()
