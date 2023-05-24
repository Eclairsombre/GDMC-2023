"""Procedural definition of the building's skelette"""

from __future__ import annotations
from Geometry.Edge import Edge
from utils.DevTools import FillPolygon,DefinePolygonVertices,FindLength
from Builder.Config import *

class Foundation():
    _polygon = []
    center = None
    
    def __init__(self,_edgeList:list[Edge]):
        self._polygon = DefinePolygonVertices(_edgeList)
        self.build()
        
    def build(self):
        self.AdjustEdges()
        self.FillFloor()
        
    def AdjustEdges(self):
        self.MakeRightAngle()
        self.SupprGreatAngles()
        self.SupprSmallAngles()
        # self.AddAngle()
        pass
                
        
    def FillFloor(self):
        FillPolygon(self._polygon)
        
    def MakeRightAngle(self):
        for _edge in self._polygon._edgeList:
            if _edge.angle > RIGHT_ANGLE[0] and _edge.angle < RIGHT_ANGLE[1] :
                _edgeToMove = self.AlignToClosestEdge(_edge)
                _destination = self._polygon.DefineIntersection(_edge,_edgeToMove)
                self._polygon.MoveEdge(_edgeToMove,_destination.GetPositionInTuple())
    
    def SupprGreatAngles(self):
        for _edge in self._polygon._edgeList:
            if _edge.angle >= MAX_ANGLE:
                _edge._previousEdge.SetNextEdge(_edge._nextEdge)
                _edge._nextEdge.SetPreviousEdge(_edge._previousEdge)
                self._polygon.removeEdge(_edge)
                
    def SupprSmallAngles(self):
        for _edge in self._polygon._edgeList:
            if _edge.angle <= MIN_ANGLE:
                if _edge._previousVertice.length <= MIN_CUT_DISTANCE or _edge._nextVertice.length <= MIN_CUT_DISTANCE:
                    self.AlignInVertice(_edge)
                elif FindLength(_edge,Edge(_edge._nextVertice.GetCenter())) <= MIN_CUT_DISTANCE or FindLength(_edge,Edge(_edge._previousVertice.GetCenter())) <= MIN_CUT_DISTANCE:
                    # Crée une nouvelle vertice qui part du centre de la plus petite des deux
                    pass
                else :
                    # Crée une nouvelle vertice dans la bonne direction avec une distance égale à MIN_CUT_DISTANCE
                    pass
                            
    def AlignToClosestEdge(self,_edge:Edge):
        _closestAlignment = -1
        _closest,_edgeToMove = None,None
        
        _distance = abs(_edge.x-_edge._previousEdge.x)
        if _distance < _closestAlignment or _closestAlignment == -1 :
            _closest,_edgeToMove = _edge._previousEdge,_edge._nextEdge
            _closestAlignment = _distance
        
        _distance = abs(_edge.x-_edge._nextEdge.x)    
        if _edge._nextEdge.x < _closestAlignment :
            _closest,_edgeToMove = _edge._nextEdge,_edge._previousEdge
            _closestAlignment = _distance
        
        _distance = abs(_edge.y-_edge._previousEdge.y)    
        if _edge._previousEdge.y < _closestAlignment :
            _closest,_edgeToMove = _edge._previousEdge,_edge._nextEdge
            _closestAlignment = _distance
        
        _distance = abs(_edge.y-_edge._nextEdge.y)    
        if _edge._nextEdge.y < _closestAlignment :
            _closest,_edgeToMove = _edge._nextEdge,_edge._previousEdge
            _closestAlignment = _distance
            
        _newLocation = self._polygon.DefineIntersection(_edge,_closest)
            
        if FindLength(_edge,_newLocation) <= FindLength(_closest,_newLocation):
            self._polygon.MoveEdge(_edge,_newLocation.GetPositionInTuple())
        else:
            self._polygon.MoveEdge(_closest,_newLocation.GetPositionInTuple())
            
        return _edgeToMove
    
    def AlignInVertice(self,_edge:Edge):
        _vertice,_edgeToAlign = None,None
        
        if _edge._previousVertice.length <  _edge._nextVertice.length:
            _vertice,_edgeToAlign = _edge._nextVertice, _edge._previousEdge
        else:
            _vertice,_edgeToAlign = _edge._previousVertice,_edge._nextEdge
        
        _intersections =_vertice.GetIntersections(_edgeToAlign.x,None,_edgeToAlign.y)
        for _intersec in _intersections:
            if _intersec != None and self._polygon.IsInPolygon(Edge(_intersec)):
                self._polygon.MoveEdge(_edge,_intersec)