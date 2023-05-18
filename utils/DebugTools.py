"""Multiple tools to help for the development
    Used for debug and test but not in the Generator"""
    
from __future__ import annotations
from gdpc import *
from gdpc.geometry import *

e = Editor()

def GetShape(pos1:tuple[int],pos2:tuple[int]):
    """Detect pink wool in the area and return their position in a tuple list"""
    _vectorList = []
    
    _direction = _GetDirection(pos1[0],pos2[0])
    for xPos in range(pos1[0]-_direction,pos2[0]+_direction,_direction) :
        _direction = _GetDirection(pos1[1],pos2[1])
        for yPos in range(pos1[1]-_direction,pos2[1]+_direction,_direction) : 
            _direction = _GetDirection(pos1[2],pos2[2])
            for zPos in range(pos1[2]-_direction,pos2[2]+_direction,_direction):
                thisBlock = e.getBlockGlobal((xPos,yPos,zPos))
                
                if thisBlock.id == "minecraft:pink_wool":
                    _vectorList.append((xPos,yPos,zPos))
                    
    return _vectorList


def _GetDirection(a,b):
    if a < b :
        return 1
    return -1


def Cut(pos1,pos2):
    placeCuboid(e,pos1,pos2,Block("minecraft:air"))