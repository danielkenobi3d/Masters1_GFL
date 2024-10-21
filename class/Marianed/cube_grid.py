import pymel.core as pm

for indexX in range(6):
    print('value of each is : {}'.format(index))
    for x_index in range(6):
        transform_node, creation = pm.polyCube(name='C_polycube{}_MSH'.format(index))
        transform_node.translateX.set(index*1.5)
        transform_node.translateY.set(y_index*1.5)
        transform_node.translateZ.set(y_index*1.5) 

for indexY in range(6):
    print('value of each is : {}'.format(index))
    for y_indexY in range(6):
        transform_node, creation = pm.polyCube(name='C_polycube{}_MSH'.format(index))
        transform_node.translateX.set(index*1.5)
        transform_node.translateY.set(z_index*1.5)
        transform_node.translateZ.set(z_index*1.5) 

for indexZ in range(6):
    print('value of each is : {}'.format(index))
    for Z_indexZ in range(6):
        transform_node, creation = pm.polyCube(name='C_polycube{}_MSH'.format(index))
        transform_node.translateX.set(index*1.5)
        transform_node.translateY.set(y_index*1.5)
        transform_node.translateZ.set(y_index*1.5) 


size_x = 6
size_y = 6
size_z = 6

idx_cube = 0
for x_index in range(size_x):
    for y_index in range(size_y):
        for z_index in range(size_z):
            print(f'Working on the cube {idx_cube} with index X: {x_index} Y: {y_index} Z: {z_index}')
            transform_node, creation = pm.polyCube(name='C_polycube{}_MSH'.format(idx_cube))
            transform_node.translateX.set(x_index*1.5)
            transform_node.translateY.set(y_index*1.5)
            transform_node.translateZ.set(z_index*1.5) 
            idx_cube = idx_cube + 1


