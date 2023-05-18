from gdpc import *

from Generator.Constructions.buildings.building import Building
from utils.DebugTools import Cut,GetShape
from tmp.tempData import _PlotList

#Cut((23,0,14),(-25,5,-60))
#print(GetShape((-34,0,-63),(-85,1,-97)))
Cut((-80,0,-6),(-35,1,-52))

#Building(_PlotList[0])
# Building(_PlotList[1])
# Building(_PlotList[2])
Building(_PlotList[4])