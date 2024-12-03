import pymel.core as pm
from RMPY.rig import rigLineBetweenPoints

selection = pm.ls(selection=True)
line_between_points = rigLineBetweenPoints.LineBetweenPoints()
line_between_points.create_point_base(*selection)