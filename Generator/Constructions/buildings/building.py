"""Building class"""

from Generator.Constructions.buildings.foundations import Foundation

class Building:
    area = () # contain every edges of the buildings. edges must be implemented in order
    
    def __init__(self,area:tuple):
        self.area = area
        self.build()

    def build(self):
        _foundations = Foundation(self.area)
        self.area = _foundations._polygon._edgeList