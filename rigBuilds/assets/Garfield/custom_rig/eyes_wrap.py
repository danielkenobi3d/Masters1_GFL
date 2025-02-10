import pymel.core as pm
from maya.mel import eval


def build():
    for each in [['R_pupil', 'R_eye'], ['L_pupil', 'L_eye']]:
        pm.select(each)

        shrinkWrap_list = set(pm.ls(type='shrinkWrap'))
        eval('CreateShrinkWrap')
        shrinkWrap_new_list = set(pm.ls(type='shrinkWrap'))
        shrink_wrap = list(shrinkWrap_new_list.difference(shrinkWrap_list))[0]
        shrink_wrap.projection.set(4)
        shrink_wrap.offset.set(0.01)