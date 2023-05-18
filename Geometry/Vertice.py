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
    
    def ToTuple(self):
        return (self.origin,self.end)