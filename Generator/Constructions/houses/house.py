from gdpc import *
from liste_block import *
import math





def house(co1,co2,cotegarage):# ,style,etage,direction):
    tailleX=abs(co2[0])-abs(co1[0])
    hauteurMax=max(co2[1],co1[1])
    hauteurMin=min(co2[1],co1[1])
    tailleZ=abs(co2[2])-abs(co1[2])
    midtailleX=tailleX//2
    midtailleZ=tailleZ//2
    editor = Editor(buffering=  True)
   
    for i in range(tailleX):
        for j in range(tailleZ):
            if cotegarage=='right':
               if i<midtailleX and j<midtailleZ:
                   editor.placeBlock((i,hauteurMin,j),grass_block)
                   if j==2 :
                       editor.placeBlock((i,hauteurMin,j),block_quartz)
                       
               else:
                   editor.placeBlock((i,hauteurMin,j),oak_planks)
            elif cotegarage=='left':
                if i<midtailleX and j>=midtailleZ:
                   editor.placeBlock((i,hauteurMin,j),grass_block)
                   if j==7 :
                       editor.placeBlock((i,hauteurMin,j),block_quartz)
                       
                else:
                   editor.placeBlock((i,hauteurMin,j),oak_planks)
                
            
    
        
    
if __name__=="__main__":
    
    house((0,-60,0),(10,-60,10),"right")
    
    
    
    
    
    
