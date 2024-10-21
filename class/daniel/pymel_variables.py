import pymel.core as pm
transform_node, creation = pm.polyCube()
print(transform_node)
print(creation)
creation.depth.set(10)
creation.height.set(5)
creation.width.set(2)
creation.heightBaseline.set(-1)
creation.subdivisionsDepth.set(10)
creation.subdivisionsHeight.set(5)
creation.subdivisionsWidth.set(7)
transform_node.translate.set(2,34,56)
transform_node.rotateX.set(45)
transform_node.rotateY.set(45)
transform_node.rotateZ.set(45)
transform_node.scale.set(45,2, 1)

import pymel.core as pm

for index in range(14):
    print('value of each is : {}'.format(index))
    for y_index in range(10):
        transform_node, creation = pm.polyCube(name='C_polycube{}_MSH'.format(index))
        transform_node.translateX.set(index*1.5)
        transform_node.translateY.set(y_index*1.5)

import maya.cmds as cmds

for index in range(14):
    print('value of each is : {}'.format(index))
    for y_index in range(10):
        transform_node, creation = cmds.polyCube(name='C_polycube{}_MSH'.format(index))
        cmds.setAttr('{}.translateX'.format(transform_node), index*1.5)
        cmds.setAttr('{}.translateY'.format(transform_node), y_index*1.5)
