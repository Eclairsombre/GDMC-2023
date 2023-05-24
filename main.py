from gdpc import *

from Builder.Constructions.buildings.building import Building
from utils.DebugTools import Cut,GetShape
from tmp.tempData import _PlotList
from utils.DevTools import TupleListToEdgeList

#Cut((23,0,14),(-25,5,-60))
# print(GetShape((-81,0,-54),(-37,1,-3)))
Cut((1560, 61, 635),(1579, 81, 654))

#Building(_PlotList[0])
# Building(_PlotList[1])
# Building(_PlotList[2])
Building(TupleListToEdgeList(_PlotList[4]))
Building(TupleListToEdgeList(_PlotList[5]))
