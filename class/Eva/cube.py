import pymel.core as pm
transform_node, creation = pm.polyCube()

for indexX in range(20):
    print('value of each is : {}'.format(indexX))
    for y_index in range(15):
        transform_node, creation = pm.polyCube(name='C_polycube{}_MSH'.format(index))
        transform_node.translateX.set(X_index*2)
        transform_node.translateY.set(y_index*2)
        transform_node.translatez.set(Z_index*2)
for indexY in range(10):
            print('value of each is : {}'.format(indexY))
            for x_index in range(8):
                transform_node, creation = pm.polyCube(name='C_polycube{}_MSH'.format(index))
                transform_node.translateX.set(X_index * 1.2)
                transform_node.translateY.set(y_index * 1.2)
                transform_node.translateY.set(Z_index * 1.2)


for indexZ in range(14):
            print('value of each is : {}'.format(indexZ))
            for z_index in range(10):
                transform_node, creation = pm.polyCube(name='C_polycube{}_MSH'.format(index))
                transform_node.translateX.set(X_index * 1.4)
                transform_node.translateY.set(y_index * 1.4)
                transform_node.translateY.set(Z_index * 1.4)