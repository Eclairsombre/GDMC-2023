"""Procedural definition of the building's skelette"""

from __future__ import annotations
from Geometry.Edge import Edge
from utils.DevTools import FillPolygon,DefinePolygonVertices

class Foundation():
    _edgeList = []
    
    def __init__(self,_edgeList:list[Edge]):
        self._edgeList = _edgeList
        DefinePolygonVertices(_edgeList)
        self.build()
        
    def build(self):
        self.AdjustEdges()
        self.FillFloor()
        
    def AdjustEdges(self):
        for _edge in self._edgeList:
            _angle = _edge.angle
            print(_angle)
        
    def FillFloor(self):
        FillPolygon(self._edgeList)
