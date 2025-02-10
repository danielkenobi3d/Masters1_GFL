from RMPY.rig.biped.rig import rigEyesAim



def build():
    rig_eyes = rigEyesAim.RigEyesAim()
    rig_eyes.create_point_base(u'R_eye00_reference_pnt', u'L_eye00_reference_pnt',aim_distance = 2,  type='circle')

