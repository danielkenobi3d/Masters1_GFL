from RMPY.rig import rigStaticLayer
from RMPY.rig.facial import rigJaw

# geometry = ['C_moustache01_main_msh', 'C_body00_main_msh', 'C_hair00_main_msh']
# rigStaticLayer.StaticLayer(*geometry,name='stretch')

jaw_rig = rigJaw.RigJaw()
jaw_rig.create_point_base('C_jaw01_reference_pnt', 'C_jawTip01_reference_pnt')
# jaw_rig.rename_as_skinned_joints()
