import maya.cmds as cmds


def  my_function():
    for index in range(14):
        print('value of each is : {}'.format(index))
        for y_index in range(10):
            transform_node, creation = cmds.polyCube(name='C_polycube{}_MSH'.format(index))
            cmds.setAttr('{}.translateX'.format(transform_node), index * 1.5)
            cmds.setAttr('{}.translateY'.format(transform_node), y_index * 1.5)