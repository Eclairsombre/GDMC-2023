"""Tools for for Generator"""

from __future__ import annotations
from cmath import sqrt
from gdpc import *
from gdpc.geometry import *

e = Editor()

# Static functions

def FillPolygon(_edgeList:tuple[tuple[int]],editor=e,_material=Block("minecraft:stone")):
    _vertices = DefinePolygonVertices(_edgeList)
    
    for _vertice in _vertices:
        placeLine(editor,_vertice[0],_vertice[1],_material )
    
    _center = DefinePolygonCenter(_edgeList)
    
    DefuseMaterial(_material,_center)


# Local functions

def DefinePolygonVertices(_edgeList):
    _verticeList = []
    
    for _edge in _edgeList:
        _verticeList.append(FindClosests(_edge,_edgeList))
    
    DeleteTriplons(_verticeList,_edgeList)
    return _verticeList

def DefinePolygonCenter(_polygon:tuple[tuple[int]]):
    xSum,ySum,zSum = 0,0,0
    for _edge in _polygon:
        xSum,ySum,zSum = xSum+_edge[0],ySum+_edge[1],zSum+_edge[2]
    
    factor = len(_polygon)
    return (round(xSum/factor),round(ySum/factor),round(zSum/factor))


def DefuseMaterial(_material,_position):
    if e.getBlockGlobal(_position).id != _material.id:
        e.placeBlockGlobal(_position,_material)
    
        for x in range(-1,2,2):
            DefuseMaterial(_material,(_position[0]+x,_position[1],_position[2]))
        for z in range(-1,2,2):
            DefuseMaterial(_material,(_position[0],_position[1],_position[2]+z))


def FindClosests(_edge,_edgeList):
    _closests = []
    for _secondedge in _edgeList:
        if _secondedge != _edge:
            _distance = FindLength,_edge,_secondedge
            
            if len(_closests) < 2:
                _closests.append((_secondedge,_distance))
            elif _distance < _closests[0][1]:
                _closests[1], _closests[0] = _closests[0], (_secondedge,_distance)
            elif _distance < _closests[1][1]:
                _closests[1] = (_secondedge,_distance)
    
    return (_closests[0][0],_closests[1][0])


def FindLength(pos1,pos2):
    return sqrt((pos1[0]-pos2[0])**2+(pos1[1]-pos2[1])**2+(pos1[2]-pos2[2])**2)


def DeleteTriplons(_verticeList,_edgeList):
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
        