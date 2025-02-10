from Masters1_GFL.rigBuilds.assets.Garfield.custom_rig import eyes_wrap
import importlib
importlib.reload(eyes_wrap)


def custom_finalize():
    eyes_wrap.build()