"""Tools for for Generator"""

from __future__ import annotations
from math import sqrt
from gdpc import *
from gdpc.geometry import *

from Geometry.Edge import Edge

e = Editor()

# Static functions


def TupleListToEdgeList(_tupleList:list[tuple[int]]):
    _edgeList = []
    for _tuple in _tupleList:
        _edgeList.append(Edge(_tuple[0],_tuple[1],_tuple[2]))
    return _edgeList


def FillPolygon(_edgeList:list[Edge],editor=e,_material:Block=Block("minecraft:stone")):
    """Permit to fill a polygon delimited by vertices with a defusion algorithme"""
    for _edge in _edgeList:
        placeLine(editor,_edge.GetPositionInTuple(),_edge._nextEdge.GetPositionInTuple(),_material )
    
    _center = DefinePolygonCenter(_edgeList)
    
    # DefuseMaterial(_material,_center)

        
def DefinePolygonVertices(_edgeList:list[Edge]):
    """Return a list of vertices from a list of edges"""
    _verticeList = []
    
    for _edge in _edgeList:
        _closests = FindClosests(_edge,_edgeList)
        _newVertice1,_newVertice2 = (_edge,_closests[0]),(_edge,_closests[1])
        _verticeList.append(SortEdgesInVertices(_newVertice1))
        _verticeList.append(SortEdgesInVertices(_newVertice2))
    
    _verticeList = DeleteIdenticalVertices(_verticeList)
    DeleteTriplons(_verticeList,_edgeList)
    Setvertices(_edgeList,_verticeList)


# Local functions


def DefinePolygonCenter(_polygon:list[Edge]):
    """calcul and return the center of the polygon"""
    xSum,ySum,zSum = 0,0,0
    for _edge in _polygon:
        xSum,ySum,zSum = xSum+_edge.x,ySum+_edge.y,zSum+_edge.z
    
    factor = len(_polygon)
    return Edge(round(xSum/factor),round(ySum/factor),round(zSum/factor))
        

def FindLength(edge1,edge2):
    """return length between the two Edges"""
    return sqrt((edge1.x-edge2.x)**2+(edge1.y-edge2.y)**2+(edge1.z-edge2.z)**2)
        

def DefuseMaterial(_material,_position:Edge):
    """defusion algorithme that defuse a material to fill a polygon"""
    _positionTuple = _position.GetPositionInTuple()
    if e.getBlockGlobal(_positionTuple).id != _material.id:
        e.placeBlockGlobal(_positionTuple,_material)
    
        for x in range(-1,2,2):
            DefuseMaterial(_material,(_position.x+x,_position.y,_position.z))
        for z in range(-1,2,2):
            DefuseMaterial(_material,(_position.x,_position.y,_position.z+z))


def FindClosests(_edge:Edge,_edgeList:list[Edge]):
    """find the two closests Edges of _edge"""
    _closests = []
    for _secondedge in _edgeList:
        if _secondedge != _edge:
            _distance = FindLength(_edge,_secondedge)
                            
            if len(_closests) < 2:
                _closests.append((_secondedge,_distance))
                if _distance < _closests[0][1]:
                    _closests = list(reversed(_closests))
            elif _distance < _closests[0][1]:
                _closests[1], _closests[0] = _closests[0], (_secondedge,_distance)
            elif _distance < _closests[1][1]:
                _closests[1] = (_secondedge,_distance)
    
    return (_closests[0][0],_closests[1][0])


def DeleteTriplons(_verticeList,_edgeList):
    """remove vertice if their attribute appeared three times or more in the _verticeList"""
    _triplons = []
    for _edge in _edgeList:
        count = 0
        for _vertice in _verticeList:
            for _secondEdge in _vertice:
                if _secondEdge == _edge:
                    count+=1

        if count > 2:
            _triplons.append(_edge)
         
    for _vertice in _verticeList:
        if _vertice[0] in _triplons and _vertice[1] in _triplons:
            _verticeList.remove(_vertice)


def DeleteIdenticalVertices(_verticeList):
    """remove vertices that appeared twice in the list"""
    _newList = []
    for _vertice in _verticeList:
        if _vertice not in _newList:
            _newList.append(_vertice)
    return _newList
        
        
def SortEdgesInVertices(_vertice):
    """Sort points in the vertice in ascending order (x-> y-> z)"""
    _firstVertice,_secondVertice = _vertice[0].GetPositionInTuple(),_vertice[1].GetPositionInTuple()
    for index in range(3):
        if _firstVertice[index] < _secondVertice[index]:
            return _vertice
        elif _firstVertice[index] > _secondVertice[index]:
            _vertice = tuple(reversed(_vertice))
            return _vertice


def Setvertices(_edgeList:list[Edge],_vertices):
    """Set the _nextVertice and _previousVertice of each Edges contained in the _vertice list"""
    _next = _edgeList[0]
    while _next != None:
        _next = SetEdges(_next,_vertices,_edgeList)
    
    

def SetEdges(_edge:Edge,_vertices,_edgeList:list[Edge]):
    """Find and set the next Edge of _edge"""
    
    if _edge._nextEdge != None:
        return None
    
    for _vertice in _vertices:
        if _edge in _vertice and _edge._previousEdge not in _vertice:
            for _tempEdge in _vertice:
                if _tempEdge != _edge:
                    _next = GetEdgeByPosition(_tempEdge.GetPositionInTuple(),_edgeList)
                    _edge.SetNextEdge(_next)
                    _next.SetPreviousEdge(_edge)
                    return _next
                
    
def GetEdgeByPosition(_position:tuple[int],_edgeList:list[Edge]):
    """return the edge with the same position as _position"""
    for _edge in _edgeList:
        if _edge.GetPositionInTuple() == _position:
            return _edge
    
        
"""def DefinePolygonVertices(_edgeList,_distance=0,_verticeList = [],):    
    _origin = _edgeList[0]
    _tempVerticeList = []
    _tempDistance = 0
    
    for _index,_edge in enumerate(_edgeList[1:]):
        _vertice = (_origin,_edge)
        _tempDistance = FindLength(_origin,_edge)
        _tempEdgeList = _edgeList[1:]
        _tempEdgeList[0],_tempEdgeList[_index] = _tempEdgeList[_index],_tempEdgeList[0]
        
        _polygon = DefinePolygonVertices(_tempEdgeList,_tempDistance,_verticeList+[_vertice])
        
        if _polygon[1] < _tempDistance or _tempVerticeList == []:
            _tempVerticeList = _polygon[0]
            _tempDistance = _polygon[1]
       
    return (_verticeList+_tempVerticeList,_distance+_tempDistance)"""