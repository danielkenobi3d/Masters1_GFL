import maya.cmds as cmds


def my_function(*args, **kwargs):
    z_value = args[0]
    x_number = kwargs.pop('x_number', 2)
    y_number = kwargs.pop('y_number', 2)

    for index in range(x_number):
        print('value of each is : {}'.format(index))
        for y_index in range(y_number):
            transform_node, creation = cmds.polyCube(name='C_polycube{}_MSH'.format(index))
            cmds.setAttr('{}.translateX'.format(transform_node), index * 1.5)
            cmds.setAttr('{}.translateY'.format(transform_node), y_index * 1.5)
            cmds.setAttr('{}.translateZ'.format(transform_node), z_value)


my_function(0, 5, 654, 7, 45576, x_number=4, y_number=5)
my_function(5, )
my_function(10, )
my_function(15, )
