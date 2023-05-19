"""Define the Vertice object"""

from __future__ import annotations
from math import sqrt

class Vertice:
    origin = (0,0,0)
    end = (0,0,0)
    length = 0
    
    def __init__(self,origin:tuple[int],end:tuple[int]) :
        self.origin = origin
        self.end = end
        self.lenght = self.SetLength()
        
    def SetLength(self):
        self.length = sqrt((self.origin[0]-self.end[0])**2+(self.origin[1]-self.end[1])**2+(self.origin[2]-self.end[2])**2)
        
    def SetOrigin(self,newOrigin:tuple[int]):
        self.origin = newOrigin
        self.SetLength()
        
    def SetEnd(self,newEnd:tuple[int]):
        self.end = newEnd
        self.SetLength()
        
    def GetIntersections(self,x=None,y=None,z=None):
        _intersecX = ()
        if self.origin[0] == self.end[0] or x == None:
            _intersecX = None
        else:
            fraction = (x - self.origin[0]) / (self.end[0] - self.origin[0])
            
            _intersecX = (x,self.origin[1] + fraction * (self.end[1] - self.origin[1]),self.origin[2] + fraction * (self.end[2] - self.origin[2]))
            
        _intersecY = ()
        if self.origin[1] == self.end[1] or y == None:
            _intersecY = None
        else:
            fraction = (y - self.origin[1]) / (self.end[1] - self.origin[1])
            
            _intersecY = (self.origin[0] + fraction * (self.end[0] - self.origin[0]),y,self.origin[2] + fraction * (self.end[2] - self.origin[2]))
        
        intersecZ = ()
        if self.origin[2] == self.end[2] or z == None:
            _intersecZ = None
        else:
            fraction = (z - self.origin[2]) / (self.end[2] - self.origin[2])
            
            _intersecZ = (self.origin[0] + fraction * (self.end[0] - self.origin[0]),self.origin[1] + fraction * (self.end[1] - self.origin[1]),z)

        return (_intersecX,_intersecY,_intersecZ)
        
    def GetCenter(self):
        return tuple(map(lambda originPos,endPos: originPos+endPos/2,self.origin,self.end))        
    
    def ToTuple(self):
        return (self.origin,self.end)
    