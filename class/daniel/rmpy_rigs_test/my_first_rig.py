from RMPY.rig import rigSingleJoint
from RMPY.rig import rigFK
from RMPY.rig import rigIK
from RMPY.rig import rigLaces
from RMPY.rig import rigLaceRing
import importlib
importlib.reload(rigIK)
import pymel.core as pm

base_points = pm.ls('C_test00_reference_pnt', 'C_test01_reference_pnt', 'C_test02_reference_pnt', 'C_test03_reference_pnt', 'C_test04_reference_pnt')
#

belt_root_points_parent= pm.ls('C_belt00_reference_grp')[0]
my_rig = rigLaceRing.LaceRing()
# my_rig = rigSingleJoint.RigSingleJoint()
# my_rig.create_point_base(*base_points, curve_distance = 1,  fk_controls = True)
my_rig.create_point_base(*belt_root_points_parent.getChildren(),
                         curve_distance = 1,
                         create_path_surface = True,
                         nurbs_to_poly_output = True, periodic=True,
                         r_l_order_change=True)



