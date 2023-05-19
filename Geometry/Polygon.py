"""Define the Polygon object"""

from __future__ import annotations
from Geometry.Edge import Edge


class Polygon:
    _edgeList = []
    _center = []
    
    def __init__(self,_edgeList:list[Edge]) :
        self._edgeList = _edgeList
        self.DefinePolygonCenter()
        
    def DefinePolygonCenter(self):
        """calcul and return the center of the polygon"""
        xSum,ySum,zSum = 0,0,0
        for _edge in self._edgeList:
            xSum,ySum,zSum = xSum+_edge.x,ySum+_edge.y,zSum+_edge.z
        
        factor = len(self._edgeList)
        self._center = Edge((round(xSum/factor),round(ySum/factor),round(zSum/factor)))
    
    def removeEdge(self,_edge):
        self._edgeList.remove(_edge)
        self.DefinePolygonCenter()
    
    def MoveEdge(self,_edge:Edge,newPos:tuple[int]):
        _edge.SetPosition(newPos)
        self.DefinePolygonCenter()
        
    def DefineIntersection(self,_edge1:Edge,_edge2:Edge):
        intersec1 = Edge((_edge1.x,_edge1.y,_edge2.z))
        intersec2 = Edge((_edge2.x,_edge2.y,_edge1.z))
        
        if _edge1.GetPositionInTuple() != intersec1.GetPositionInTuple() and _edge1.GetPositionInTuple() != intersec2.GetPositionInTuple():
            if self.IsInPolygon(intersec1):
                return intersec1
        return intersec2
        
    def IsInPolygon(self,_edge:Edge):
        _angleSum = 0
        
        for _polygonEdge in self._edgeList:
            _edge.SetNextEdge(_polygonEdge._nextEdge)
            _edge.SetPreviousEdge(_polygonEdge)
            _angleSum += _edge.angle
            
        return _angleSum == 360
        