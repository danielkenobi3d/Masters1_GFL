from Masters1_GFL.rigBuilds.assets.Garfield.custom_rig import rigBiped
import importlib
importlib.reload(rigBiped)
import pymel.core as pm


def build_biped_rig():
    rig_biped = rigBiped.RigByped()
    rig_biped.build()
    geo_root = pm.ls('geo', 'GEO')
    if geo_root:
        pm.parent(geo_root, 'rig')
    pm.parent('environment', 'rig')


def custom_rig():
    pass