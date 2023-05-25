from gdpc import *
from liste_block import *
import math
import time



def delete(co1,co2):
    editor = Editor(buffering=  True) 
    x=abs((co2[0])-(co1[0]))
    z=abs((co2[2])-(co1[2]))
    y= abs(co2[1]-co1[1])
    for i in range(y):
            for j in range(z):
                for a in range(x):
                    editor.placeBlock((co1[0]+a,co1[1]+i,co1[2]+j),air)


def mur_sol(co1,co2,block):
    editor = Editor(buffering=  True) 
    
    if co1[1]==co2[1]:
         for i in range(abs(abs(co2[0])-abs(co1[0]))):
            for j in range((abs(co2[2])-abs(co1[2]))):
                editor.placeBlock((co1[0]+i,co1[1],co1[2]+j),block)
    elif co2[0]==co1[0]:
       
        for i in range(abs(abs(co2[1])-abs(co1[1]))):
            for j in range((abs(co2[2])-abs(co1[2]))):
               
                editor.placeBlock((co1[0],co1[1]+i,co1[2]+j),block)
                
    elif co2[2]==co1[2]:
        for i in range(abs(abs(co2[1])-abs(co1[1]))):
            for j in range((abs(co2[0])-abs(co1[0]))):
            
                editor.placeBlock((co1[0]+j,co1[1]+i,co1[2]),block)
                
    
def poserEscalier(co1,co2,type):
    editor = Editor(buffering=  True) 
    if co1[0]==co2[0]:
        for i in range((abs(co2[2])-abs(co1[2]))):
            editor.placeBlock((co1[0],co1[1],co1[2]+i),type)
    if co1[2]==co2[2]:
        for i in range((abs(co2[0])-abs(co1[0]))):
            editor.placeBlock((co1[0]+i,co1[1],co1[2]),type)
     
                
def poserPorte(co,type):
    editor = Editor(buffering=  True) 
    editor.placeBlock((co[0],co[1],co[2]),type)
    
    
    
def poserToit(co1,co2,hauteurMax):
    x1=co1[0]
    y1=co1[1]
    z1=co1[2]
    x2=co2[0]
    y2=co2[1]
    z2=co2[2]
    tailleX=abs(co2[0])-abs(co1[0])
   
    tailleZ=abs(co2[2])-abs(co1[2])
    midtailleX=tailleX//2
    midtailleZ=tailleZ//2
    for i in range(4):
        mur_sol((x1,y1+5+i,z1+i),(x2-i,y1+5+i,midtailleZ-i),oak_planks)
        mur_sol((midtailleX+i,y1+5+i,midtailleZ-i),(x2-i,y1+5+i,z2),oak_planks)
        poserEscalier((x1,y1+5+i,z1-1+i),(x2+1-i,y1+5+i,z1-1+i),stairs_gauche)
        poserEscalier((x2-i,y1+5+i,z1+i),(x2-i,y1+5+i,z2),stairs_derriere)
        poserEscalier((x1,y1+5+i,midtailleZ-i),(midtailleX+i,y1+5+i,midtailleZ-i),stairs_droite)
        poserEscalier((midtailleX-1+i,y1+5+i,midtailleZ+1-i),(midtailleX-1+i,y1+5+i,z2),stairs_devant)
        if hauteurMax==5+i:
            break
        
    
def poserFenetre(co1,co2,type):
    editor = Editor(buffering=  True) 
    x=abs((co2[0])-(co1[0]))
    z=abs((co2[2])-(co1[2]))
    y= abs(co2[1]-co1[1])
    print(x)
    if co1[0]==co2[0]:
        if z%2==0:
            for i in range(z//2):
                if i%2==0:
                    editor.placeBlock((co1[0],co1[1]+1,co1[2]+i*2+1),type)
                    editor.placeBlock((co1[0],co1[1]+1,co1[2]+i*2+2),type)
        else:
            for i in range(z):
                if i%2==0:
                    editor.placeBlock((co1[0],co1[1]+1,co1[2]+i),type)
                    
                    
                
            
    if co1[2]==co2[2]:
        if x%2==0:
            for i in range(x//2):
                if i%2==0:
                    editor.placeBlock((co1[0]+i*2+1,co1[1]+1,co1[2]),type)
                    editor.placeBlock((co1[0]+i*2+2,co1[1]+1,co1[2]),type)
        else:
            for i in range(x):
                if i%2==0:
                    editor.placeBlock((co1[0]+i,co1[1]+1,co1[2]),type)
    

def house(co1,co2,cotegarage,hauteurMax):# ,style,etage,direction):
    """
    Minimun 10*10 
    """
    tailleX=abs(co2[0])-abs(co1[0])
    
    hauteurMin=min(co2[1],co1[1])
    tailleZ=abs(co2[2])-abs(co1[2])
    midtailleX=tailleX//2
    midtailleZ=tailleZ//2
    editor = Editor(buffering=  True) 
    
    x1=co1[0]
    y1=co1[1]
    z1=co1[2]
    x2=co2[0]
    y2=co2[1]
    z2=co2[2]
    
    
    
            
    for i in range(tailleX):
        for j in range(tailleZ):
            if cotegarage=='right':
               if i<midtailleX and j<midtailleZ:

                
                   if midtailleZ%2==0:
                        if j==midtailleZ//2 or j==(midtailleZ//2)-1 :
                            editor.placeBlock((x1+i,hauteurMin,z1+j),block_quartz)
                            
                            
                   else:
                       if j==midtailleZ//2 :
                            editor.placeBlock((x1+i,hauteurMin,z1+j),block_quartz)
                           
                   
                            
               
            elif cotegarage=='left':
                
                if i<midtailleX and j>=midtailleZ:
                   
                   if (tailleZ-midtailleZ)%2==0:
                        if j==tailleZ-(midtailleZ//2)-2 or j==tailleZ-(midtailleZ//2)-1 :
                            editor.placeBlock((x1+i,hauteurMin,z1+j),block_quartz)
                        
                            
                   else:
                       if j==tailleZ-(midtailleZ//2) -1:
                            editor.placeBlock((x1+i,hauteurMin,z1+j),block_quartz)
                    
                   
                            
    
    
    #murs
    mur_sol((x1,y1+1,z1),(x2,y1+5,z1),block_quartz)
    mur_sol((x1,y1+1,z1),(x1,y1+5,midtailleZ   ),block_quartz)
    mur_sol((x2-1,y1+1,z1),(x2-1,y1+5,z2),block_quartz)
    mur_sol((x1,y1+1,midtailleZ-1),(midtailleX+1,y1+5,midtailleZ-1),block_quartz)
    mur_sol((midtailleX,y1+1,midtailleZ),(midtailleX,y1+5,z2),block_quartz)
    mur_sol((midtailleX,y1+1,z2-1),(x2,y1+5,z2-1),block_quartz)
    
    
    #sols/plafonds
    mur_sol((x1,y1+4,z1),(x2,y1+4,midtailleZ),block_quartz)
    mur_sol((x1,y1,z1),(x2,y1,midtailleZ),oak_planks)
    mur_sol((midtailleX,y1+4,midtailleZ),(x2,y1+4,z2),block_quartz)
    mur_sol((midtailleX,y1,midtailleZ),(x2,y1,z2),oak_planks)
    mur_sol((x1,y1,midtailleZ),(midtailleX,y1,z2),grass_block)
    
    poserFenetre((midtailleX,y1+1,midtailleZ+1),(midtailleX,y1+5,z2-1),glass)
    poserFenetre((x2-1,y1+1,z1+1),(x2-1,y1+5,z2-1),glass)
    poserFenetre((midtailleX,y1+1,z2-1),(x2,y1+5,z2-1),glass)
    poserFenetre((x1+2,y1+1,z1),(x2-1,y1+5,z1),glass)
    
    
    
    if cotegarage=='left':
        if (tailleZ-midtailleZ)%2==0:
            
            poserPorte((midtailleX,hauteurMin+1,z2-((midtailleZ)//2)-1),door_east)
            poserPorte((midtailleX,hauteurMin+1,z2-((midtailleZ)//2)-2),door_east)
        else:
            poserPorte((midtailleX,hauteurMin+1,z2-((midtailleZ)//2)-1),door_east)
            
            
    poserToit(co1,co2,hauteurMax)    
    
   
   
    
    
    
if __name__=="__main__":
    
    house((0,-60,0),(15,-60,14),"left",7)
    
    #delete((-10,-60,-10),(20,-40,20))
    

    
    
    
    
    
