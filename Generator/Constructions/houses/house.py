from gdpc import *
from liste_block import *

editor = Editor(buffering=True)

editor.placeBlock((0,-60,0),oak_planks)


def house(co1,co2):# ,style,cotegarage,etage,direction):
    tailleX=abs(co2[0])-abs(co1[0])
    hauteur=max(co2[1],co1[1])
    tailleZ=abs(co2[2])-abs(co1[2])
    print(tailleZ)
    for i in range(tailleX):
        for j in range(tailleZ):
            editor.placeBlock((i,-59,j),oak_planks)
            
    
    
    
    
    
    
    
    
if __name__=="__main__":
    
    house((0,-60,0),(10,-60,10))