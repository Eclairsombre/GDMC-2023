"""Procedural definition of the building's skelette"""

from utils.DevTools import FillPolygon

class Foundation():
    area = []
    
    def __init__(self,area:list):
        self.area = area
        self.build()
        
    def build(self):
        self.AdjustEdges()
        self.FillFloor(self.area)
        
    def AdjustEdges(self):
        for _edge in self.area:
            pass
        
    def FillFloor(self,_edgeList):
        FillPolygon(_edgeList)
