from RMPY.rig import rigBase
from RMPY.rig import rigLaceRing
from RMPY.rig import rigFK
import pymel.core as pm



class RigTailModel(rigBase.BaseModel):
    def __init__(self):
        super(RigTailModel, self).__init__()
        self.rig_tail_fk = None
        self.rig_tail_ik = None


class RigTail(rigBase.RigBase):
    def __init__(self, *args, **kwargs):
        kwargs['model'] = kwargs.pop('model', RigTailModel())
        super(RigTail, self).__init__(*args, **kwargs)

    def create_point_base(self, *args, **kwargs):
        self._model.rig_tail_fk = rigFK.RigFK(rig_system = self.rig_system)
        self.rig_tail_fk.create_point_base(*args, name='fkTail')

        self._model.rig_tail_ik = rigLaceRing.LaceRing(rig_system=self.rig_system)
        self.rig_tail_ik.create_point_base(*args,
                                   create_path_surface=True,
                                   centered=True, curve_distance=.1, nurbs_to_poly_output=True, name='ikTail')

        pm.skinCluster(self.rig_tail_fk.joints, self.rig_tail_ik.geometry_output)
        # create_path_surface=True, controls_number=6,

        self.rig_tail_fk.set_parent('C_main01_Hip_sknjnt')
        self.joints.extend(self.rig_tail_ik.lace_rig.joints)
        self.root = self.rig_tail_fk.root

