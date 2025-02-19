from Masters1_GFL.rigBuilds.assets.rigClass.custom_rig import rigBiped
import pymel.core as pm
from Masters1_GFL.rigBuilds.assets.John.custom_rig import eyes_rig
import importlib
importlib.reload(eyes_rig)

def build_biped_rig():
    rig_biped = rigBiped.RigByped()
    rig_biped.build()
    geo_root = pm.ls('geo', 'GEO')
    if geo_root:
        pm.parent(geo_root, 'rig')
    pm.parent('environment', 'rig')


def custom_rig():
    eyes_rig.build()