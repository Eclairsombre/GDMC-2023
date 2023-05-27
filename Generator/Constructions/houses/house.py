from gdpc import *
from liste_block import *



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
         for i in range(abs(co2[0]-(co1[0]))):
            for j in range((abs((co2[2])-(co1[2])))):
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
    
    
    
def poserToit(co1,co2,hauteurMax,cotegarage):
    x1=co1[0]
    y1=co1[1]
    z1=co1[2]
    x2=co2[0]
    y2=co2[1]
    z2=co2[2]
    
    tailleX=abs(co2[0])-abs(co1[0])
    editor = Editor(buffering=  True) 
    tailleZ=abs(co2[2])-abs(co1[2])
    midtailleX=(tailleX//2)+x1
    midtailleZ=(tailleZ//2)+z1
    if cotegarage=='left':
        if x1==0 and z1==0:
            for i in range(3):
                if i==2:
                    mur_sol((x1-1,y1+4+i,z1+i),(x2-i,y1+4+i,midtailleZ-i),oak_planks)
                    mur_sol((midtailleX+i,y1+4+i,midtailleZ-i),(x2-i,y1+4+i,z2+1),oak_planks)
                    mur_sol((x1-1,y1+5+i,z1+i),(x2-i,y1+5+i,midtailleZ-i),oak_slab)
                    mur_sol((midtailleX+i,y1+5+i,midtailleZ-i),(x2-i,y1+5+i,z2+1),oak_slab)
                    
                else:
                    mur_sol((x1,y1+4+i,z1+i),(x2-i,y1+4+i,midtailleZ-i),block_white_concrete)
                    mur_sol((midtailleX+i,y1+4+i,midtailleZ-i),(x2-i,y1+4+i,z2),block_white_concrete)
                    
                poserEscalier((x1-1,y1+4+i,z1-1+i),(x2+3-i,y1+4+i,z1-1+i),stairs_gauche)
                poserEscalier((x2-i,y1+4+i,z1+i),(x2-i,y1+4+i,z2+1),stairs_derriere)
                poserEscalier((x1-1,y1+4+i,midtailleZ-i),(midtailleX+2+i,y1+4+i,midtailleZ-i),stairs_droite)
                poserEscalier((midtailleX-1+i,y1+4+i,midtailleZ+1-i),(midtailleX-1+i,y1+4+i,z2+1),stairs_devant)
                if hauteurMax==5+i:
                    break
            for i in range(2):
                editor.placeBlock((x1-1,y1+4+i,z1+i),stairs_droite_retourner)
                editor.placeBlock((x1-1,y1+4+i,midtailleZ-i-1),stairs_gauche_retourner)
                editor.placeBlock((x2-1-i,y1+4+i,z2),stairs_devant_retourner)
                editor.placeBlock((midtailleX+i,y1+4+i,z2),stairs_derriere_retourner)
        elif x1==0:
            for i in range(3):
                if i==2:
                    mur_sol((x1-1,y1+4+i,z1+i),(x2+2-i,y1+4+i,midtailleZ-i),oak_planks)
                    mur_sol((midtailleX+i,y1+4+i,midtailleZ-i),(x2-i,y1+4+i,z2+1),oak_planks)
                    mur_sol((x1-1,y1+5+i,z1+i),(x2+2-i,y1+5+i,midtailleZ-i),oak_slab)
                    mur_sol((midtailleX+i,y1+5+i,midtailleZ-i),(x2-i,y1+5+i,z2+1),oak_slab)
                    
                else:
                    mur_sol((x1,y1+4+i,z1+i),(x2-i,y1+4+i,midtailleZ-i),block_white_concrete)
                    mur_sol((midtailleX+i,y1+4+i,midtailleZ-i),(x2-i,y1+4+i,z2),block_white_concrete)
                    
                poserEscalier((x1-1,y1+4+i,z1-1+i),(x2+3-i,y1+4+i,z1-1+i),stairs_gauche)
                poserEscalier((x2-i,y1+4+i,z1+i),(x2-i,y1+4+i,z2+1),stairs_derriere)
                poserEscalier((x1-1,y1+4+i,midtailleZ-i),(midtailleX+2+i,y1+4+i,midtailleZ-i),stairs_droite)
                poserEscalier((midtailleX-1+i,y1+4+i,midtailleZ+1-i),(midtailleX-1+i,y1+4+i,z2+1),stairs_devant)
                if hauteurMax==5+i:
                    break
            for i in range(2):
                editor.placeBlock((x1-1,y1+4+i,z1+i),stairs_droite_retourner)
                editor.placeBlock((x1-1,y1+4+i,midtailleZ-i-1),stairs_gauche_retourner)
                editor.placeBlock((x2-1-i,y1+4+i,z2),stairs_devant_retourner)
                editor.placeBlock((midtailleX+i,y1+4+i,z2),stairs_derriere_retourner)
                
        elif  z1==0:
            for i in range(3):
                if i==2:
                    mur_sol((x1-1,y1+4+i,z1+i),(x2-i,y1+4+i,midtailleZ-i),oak_planks)
                    mur_sol((midtailleX+i,y1+4+i,midtailleZ-i),(x2-i,y1+4+i,z2+1),oak_planks)
                    mur_sol((x1-1,y1+5+i,z1+i),(x2-i,y1+5+i,midtailleZ-i),oak_slab)
                    mur_sol((midtailleX+i,y1+5+i,midtailleZ-i),(x2-i,y1+5+i,z2+1),oak_slab)
                    
                else:
                    mur_sol((x1,y1+4+i,z1+i),(x2-i,y1+4+i,midtailleZ-i),block_white_concrete)
                    mur_sol((midtailleX+i,y1+4+i,midtailleZ-i),(x2-i,y1+4+i,z2),block_white_concrete)
                    
                poserEscalier((x1-1,y1+4+i,z1-1+i),(x2+1-i,y1+4+i,z1-1+i),stairs_gauche)
                poserEscalier((x2-i,y1+4+i,z1+i),(x2-i,y1+4+i,z2+1),stairs_derriere)
                poserEscalier((x1-1,y1+4+i,midtailleZ-i),(midtailleX+i,y1+4+i,midtailleZ-i),stairs_droite)
                poserEscalier((midtailleX-1+i,y1+4+i,midtailleZ+1-i),(midtailleX-1+i,y1+4+i,z2+1),stairs_devant)
                if hauteurMax==5+i:
                    break
            for i in range(2):
                editor.placeBlock((x1-1,y1+4+i,z1+i),stairs_droite_retourner)
                editor.placeBlock((x1-1,y1+4+i,midtailleZ-i-1),stairs_gauche_retourner)
                editor.placeBlock((x2-1-i,y1+4+i,z2),stairs_devant_retourner)
                editor.placeBlock((midtailleX+i,y1+4+i,z2),stairs_derriere_retourner)
            
        
        
        
        else:
            for i in range(3):
                if i==2:
                    mur_sol((x1-1,y1+4+i,z1+i),(x2-i,y1+4+i,midtailleZ-i),oak_planks)
                    mur_sol((midtailleX+i,y1+4+i,midtailleZ-i),(x2-i,y1+4+i,z2+1),oak_planks)
                    mur_sol((x1-1,y1+5+i,z1+i),(x2-i,y1+5+i,midtailleZ-i),oak_slab)
                    mur_sol((midtailleX+i,y1+5+i,midtailleZ-i),(x2-i,y1+5+i,z2+1),oak_slab)
                    
                else:
                    mur_sol((x1,y1+4+i,z1+i),(x2-i,y1+4+i,midtailleZ-i),block_white_concrete)
                    mur_sol((midtailleX+i,y1+4+i,midtailleZ-i),(x2-i,y1+4+i,z2),block_white_concrete)
                    
                    
                poserEscalier((x1-1,y1+4+i,z1-1+i),(x2+1-i,y1+4+i,z1-1+i),stairs_gauche)
                poserEscalier((x2-i,y1+4+i,z1+i),(x2-i,y1+4+i,z2+1),stairs_derriere)
                poserEscalier((x1-1,y1+4+i,midtailleZ-i),(midtailleX+i,y1+4+i,midtailleZ-i),stairs_droite)
                poserEscalier((midtailleX-1+i,y1+4+i,midtailleZ+1-i),(midtailleX-1+i,y1+4+i,z2+1),stairs_devant)
                if hauteurMax==5+i:
                    break
            for i in range(2):
                editor.placeBlock((x1-1,y1+4+i,z1+i),stairs_droite_retourner)
                editor.placeBlock((x1-1,y1+4+i,midtailleZ-i-1),stairs_gauche_retourner)
                editor.placeBlock((x2-1-i,y1+4+i,z2),stairs_devant_retourner)
                editor.placeBlock((midtailleX+i,y1+4+i,z2),stairs_derriere_retourner)
            
   
    elif cotegarage=='right':
        if x1==0 and z1==0:
           
            for i in range(3):
                if i==2:
                    
                    
                    mur_sol((midtailleX+i,y1+4+i,z1-1),(x2-i,y1+4+i,z2-i),oak_planks)
                    mur_sol((x1-1,y1+4+i,midtailleZ+i),(x2-i,y1+4+i,z2-i),oak_planks)
                    mur_sol((midtailleX+i,y1+5+i,z1-1),(x2-i,y1+5+i,z2-i),oak_slab)
                    mur_sol((x1-1,y1+5+i,midtailleZ+i),(x2-i,y1+5+i,z2-i),oak_slab)
                    
                else:
                    mur_sol((midtailleX+i,y1+4+i,z1),(x2-i,y1+4+i,z2-i),block_white_concrete)
                    mur_sol((x1,y1+4+i,midtailleZ+i),(x2-i,y1+4+i,z2-i),block_white_concrete)
                
                poserEscalier((x1-1,y1+4+i,midtailleZ-1+i),(midtailleX+2+i,y1+4+i,midtailleZ-1+i),stairs_gauche)
                poserEscalier((x2-i,y1+4+i,z1-1),(x2-i,y1+4+i,z2+3-i),stairs_derriere)
                poserEscalier((x1-1,y1+4+i,z2-i),(x2-i+2,y1+4-i,z2-i),stairs_droite)
                poserEscalier((midtailleX-1+i,y1+4+i,z1-1),(midtailleX-1+i,y1+4+i,midtailleZ+1+i),stairs_devant)
                if hauteurMax==5+i:
                    break
            for i in range(2):
                editor.placeBlock((midtailleX+i,y1+4+i,z1-1),stairs_derriere_retourner)
                editor.placeBlock((x2-1-i,y1+4+i,z1-1),stairs_devant_retourner)
                editor.placeBlock((x1-1,y1+4+i,midtailleZ+i),stairs_droite_retourner)
                editor.placeBlock((x1-1,y1+4+i,z2-1-i),stairs_gauche_retourner)
                pass
        elif x1==0:
            for i in range(3):
                if i==2:
                
                    
                    mur_sol((midtailleX+i,y1+4+i,z1-1),(x2-i,y1+4+i,z2-i),oak_planks)
                    mur_sol((x1-1,y1+4+i,midtailleZ+i),(x2+1-i,y1+4+i,z2-i),oak_planks)
                    mur_sol((midtailleX+i,y1+5+i,z1-1),(x2-i,y1+5+i,z2-i),oak_slab)
                    mur_sol((x1-1,y1+5+i,midtailleZ+i),(x2+1-i,y1+5+i,z2-i),oak_slab)
                    
                else:
                    mur_sol((midtailleX+i,y1+4+i,z1),(x2-i,y1+4+i,z2-i),block_white_concrete)
                    mur_sol((x1,y1+4+i,midtailleZ+i),(x2-i,y1+4+i,z2-i),block_white_concrete)
                
                poserEscalier((x1-1,y1+4+i,midtailleZ-1+i),(midtailleX+2+i,y1+4+i,midtailleZ-1+i),stairs_gauche)
                poserEscalier((x2-i,y1+4+i,z1-1),(x2-i,y1+4+i,z2+1-i),stairs_derriere)
                poserEscalier((x1-1,y1+4+i,z2-i),(x2-i+2,y1+4-i,z2-i),stairs_droite)
                poserEscalier((midtailleX-1+i,y1+4+i,z1-1),(midtailleX-1+i,y1+4+i,midtailleZ+i),stairs_devant)
                if hauteurMax==5+i:
                    break
            for i in range(2):
                editor.placeBlock((midtailleX+i,y1+4+i,z1-1),stairs_derriere_retourner)
                editor.placeBlock((x2-1-i,y1+4+i,z1-1),stairs_devant_retourner)
                editor.placeBlock((x1-1,y1+4+i,midtailleZ+i),stairs_droite_retourner)
                editor.placeBlock((x1-1,y1+4+i,z2-1-i),stairs_gauche_retourner)
                pass
            
        elif z1==0:
            
            for i in range(3):
                if i==2:
                
                    
                    mur_sol((midtailleX+i,y1+4+i,z1-1),(x2-i,y1+4+i,z2-i),oak_planks)
                    mur_sol((x1-1,y1+4+i,midtailleZ+i),(x2-i,y1+4+i,z2-i),oak_planks)
                    mur_sol((midtailleX+i,y1+5+i,z1-1),(x2-i,y1+5+i,z2-i+1),oak_slab)
                    mur_sol((x1-1,y1+5+i,midtailleZ+i),(x2-i,y1+5+i,z2-i),oak_slab)
                    
                else:
                    mur_sol((midtailleX+i,y1+4+i,z1),(x2-i,y1+4+i,z2-i),block_white_concrete)
                    mur_sol((x1,y1+4+i,midtailleZ+i),(x2-i,y1+4+i,z2-i),block_white_concrete)
                
                poserEscalier((x1-1,y1+4+i,midtailleZ-1+i),(midtailleX+i,y1+4+i,midtailleZ-1+i),stairs_gauche)
                poserEscalier((x2-i,y1+4+i,z1-1),(x2-i,y1+4+i,z2+2-i),stairs_derriere)
                poserEscalier((x1-1,y1+4+i,z2-i),(x2-i+1,y1+4-i,z2-i),stairs_droite)
                poserEscalier((midtailleX-1+i,y1+4+i,z1-1),(midtailleX-1+i,y1+4+i,midtailleZ+1+i),stairs_devant)
                if hauteurMax==5+i:
                    break
            for i in range(2):
                editor.placeBlock((midtailleX+i,y1+4+i,z1-1),stairs_derriere_retourner)
                editor.placeBlock((x2-1-i,y1+4+i,z1-1),stairs_devant_retourner)
                editor.placeBlock((x1-1,y1+4+i,midtailleZ+i),stairs_droite_retourner)
                editor.placeBlock((x1-1,y1+4+i,z2-1-i),stairs_gauche_retourner)
                
        else:
            
            for i in range(3):
                if i==2:
                
                    
                    mur_sol((midtailleX+i,y1+4+i,z1-1),(x2-i,y1+4+i,z2-i),oak_planks)
                    mur_sol((x1-1,y1+4+i,midtailleZ+i),(x2-i,y1+4+i,z2-i),oak_planks)
                    mur_sol((midtailleX+i,y1+5+i,z1-1),(x2-i,y1+5+i,z2-i),oak_slab)
                    mur_sol((x1-1,y1+5+i,midtailleZ+i),(x2-i,y1+5+i,z2-i),oak_slab)
                    
                else:
                    mur_sol((midtailleX+i,y1+4+i,z1),(x2-i,y1+4+i,z2-i),block_white_concrete)
                    mur_sol((x1,y1+4+i,midtailleZ+i),(x2-i,y1+4+i,z2-i),block_white_concrete)
                    
                    
                poserEscalier((x1-1,y1+4+i,midtailleZ-1+i),(midtailleX+i,y1+4+i,midtailleZ-1+i),stairs_gauche)
                poserEscalier((x2-i,y1+4+i,z1-1),(x2-i,y1+4+i,z2-i),stairs_derriere)
                poserEscalier((x1-1,y1+4+i,z2-i),(x2-i+1,y1+4-i,z2-i),stairs_droite)
                poserEscalier((midtailleX-1+i,y1+4+i,z1-1),(midtailleX-1+i,y1+4+i,midtailleZ+i),stairs_devant)
                if hauteurMax==5+i:
                    break
            for i in range(2):
                editor.placeBlock((midtailleX+i,y1+4+i,z1-1),stairs_derriere_retourner)
                editor.placeBlock((x2-1-i,y1+4+i,z1-1),stairs_devant_retourner)
                editor.placeBlock((x1-1,y1+4+i,midtailleZ+i),stairs_droite_retourner)
                editor.placeBlock((x1-1,y1+4+i,z2-1-i),stairs_gauche_retourner)
                pass
    
            
    
def poserFenetre(co1,co2,type):
    editor = Editor(buffering=  True) 
    
    x=abs((co2[0])-(co1[0]))
    z=abs((co2[2])-(co1[2]))
    y= abs(co2[1]-co1[1])
  
    if co1[0]==co2[0]:
        if z%2==0:
            if z==4:
                  
                    editor.placeBlock((co1[0],co1[1]+1,co1[2]+1),type)
                    editor.placeBlock((co1[0],co1[1]+1,co1[2]+2),type)
            else:
                
                for i in range(z//2):
                    if i%2==0:
                        editor.placeBlock((co1[0],co1[1]+1,co1[2]+i*2),type)
                        editor.placeBlock((co1[0],co1[1]+1,co1[2]+i*2+1),type)
        else:
            if z<=5:
                for i in range(z):
                    
                        
                        editor.placeBlock((co1[0],co1[1]+1,co1[2]+i),type)
            else:
                
                for i in range((z//3)):
                        if 3*(i+1)+(i)>abs(co2[2]-co1[2]):
                            break
                        else:
                            editor.placeBlock((co1[0],co1[1]+1,co1[2]+i*4),type)
                            editor.placeBlock((co1[0],co1[1]+1,co1[2]+i*4+1),type)
                            editor.placeBlock((co1[0],co1[1]+1,co1[2]+i*4+2),type)
                        
                    
                
            
    if co1[2]==co2[2]:
        
        if x%2==0:
            if x==4:
                  
                    editor.placeBlock((co1[0]+1,co1[1]+1,co1[2]),type)
                    editor.placeBlock((co1[0]+2,co1[1]+1,co1[2]),type)
            else:
                for i in range(x//2):
                    if i%2==0:
                        editor.placeBlock((co1[0]+i*2,co1[1]+1,co1[2]),type)
                        editor.placeBlock((co1[0]+i*2+1,co1[1]+1,co1[2]),type)
        else:
            if x<=5:
                
                 
                for i in range(x):
                        
                            
                            editor.placeBlock((co1[0]+i,co1[1]+1,co1[2]),type)
            else:
                
                for i in range((x//3)):
                        if 3*(i+1)+i>abs(co2[0]-co1[0]):
                            break
                        else:
                            editor.placeBlock((co1[0]+i*4,co1[1]+1,co1[2]),type)
                            editor.placeBlock((co1[0]+i*4+1,co1[1]+1,co1[2]),type)
                            editor.placeBlock((co1[0]+i*4+2,co1[1]+1,co1[2]),type)
            
                    
                    
                    
                    
                    

def poserGarage(co1,co2):
    editor = Editor(buffering=  True) 
    x=abs((co2[0])-(co1[0]))
    z=abs((co2[2])-(co1[2]))
    
                
    if co2[0]==co1[0]:
       
        for i in range(abs(abs(co2[1])-abs(co1[1]))):
            for j in range((abs(co2[2])-abs(co1[2]))):
               
                editor.placeBlock((co1[0],co1[1]+i,co1[2]+j),block_quartz)
                
    elif co2[2]==co1[2]:
        for i in range(abs(abs(co2[1])-abs(co1[1]))):
            for j in range((abs(co2[0])-abs(co1[0]))):
            
                editor.placeBlock((co1[0]+j,co1[1]+i,co1[2]),block_quartz)
    
    
    
    if co1[0]==co2[0]:
        
        if z%3==0:
            for i in range(z//3):
                    editor.placeBlock((co1[0],co2[1],co1[2]+i*3),stairs_quartz_droite)
                    editor.placeBlock((co1[0],co2[1],co1[2]+1+i*3),quartz_slab_up)
                    editor.placeBlock((co1[0],co2[1],co1[2]+2+i*3),stairs_quartz_gauche)
        elif z%2==0:
            for i in range(z):
                if i%2==0:
                    editor.placeBlock((co1[0],co2[1],co1[2]+i),stairs_quartz_droite)
                else:
                    editor.placeBlock((co1[0],co2[1],co1[2]+i),stairs_quartz_gauche)
        if  z%5==0:
            for i in range((z//5)):
                    
                    editor.placeBlock((co1[0],co2[1],co1[2]+i*5),stairs_quartz_droite)
                    editor.placeBlock((co1[0],co2[1],co1[2]+1+i*5),stairs_quartz_gauche)
                    editor.placeBlock((co1[0],co2[1],co1[2]+2+i*5),block_quartz)
                    editor.placeBlock((co1[0],co2[1],co1[2]+3+i*5),stairs_quartz_droite)
                    editor.placeBlock((co1[0],co2[1],co1[2]+4+i*5),stairs_quartz_gauche)
                
                    
            

                    
                
            

def house(co1,co2,cotegarage,hauteurMax):# ,style,etage,direction):
    """
    Minimun 10*10 
    """
    tailleX=abs(co2[0])-abs(co1[0])
    
    hauteurMin=min(co2[1],co1[1])
    tailleZ=abs(co2[2])-abs(co1[2])
    
    editor = Editor(buffering=  True) 
    
    print(tailleZ)
    
    x1=co1[0]
    y1=co1[1]
    z1=co1[2]
    x2=co2[0]
    y2=co2[1]
    z2=co2[2]
    midtailleX=(tailleX//2)+x1
    midtailleZ=(tailleZ//2)+z1
    
    
    if cotegarage=='right':
        
                                
                                
                             
        #murs
        poserGarage((x1+1,y1+1,midtailleZ+1),(x1+1,y1+3,z2-1))
        mur_sol((x1,y1+1,z2-1),(x2,y1+5,z2-1),block_white_concrete)
        mur_sol((x1,y1+1,midtailleZ),(x1,y1+5,z2   ),block_white_concrete)
        mur_sol((x2-1,y1+1,z1),(x2-1,y1+5,z2),block_white_concrete)
        mur_sol((x1,y1+1,midtailleZ),(midtailleX+1,y1+5,midtailleZ),block_white_concrete)
        mur_sol((midtailleX,y1+1,z1),(x2,y1+5,z1),block_white_concrete)
        mur_sol((midtailleX,y1+1,z1),(midtailleX,y1+5,midtailleZ),block_white_concrete)
        
        
        mur_sol((x1,y1+1,midtailleZ+1),(x1,y1+4,z2-1   ),air)
        
        #sols/plafonds
        mur_sol((midtailleX,y1+4,z1),(x2,y1+4,z2),block_white_concrete)
        mur_sol((midtailleX,y1,z1),(x2,y1,z2),oak_planks)
        mur_sol((x1,y1+4,midtailleZ),(midtailleX,y1+4,z2),block_white_concrete)
        mur_sol((x1,y1,midtailleZ),(midtailleX,y1,z2),oak_planks)
        mur_sol((x1,y1,z1),(midtailleX,y1,midtailleZ),grass_block)
        
      
        
        poserFenetre((midtailleX,y1+1,z1+1),(midtailleX,y1+5,midtailleZ-1),glass)
        poserFenetre((midtailleX+1,y1+1,z1),(x2-1,y1+5,z1),glass)
        poserFenetre((x1+2,y1+1,midtailleZ),(midtailleX-1,y1+5,midtailleZ),glass)
        poserFenetre((x2-1,y1+1,z1+1),(x2-1,y1+5,z2-1),glass)
        poserFenetre((x1+2,y1+1,z2-1),(x2-1,y1+4,z2-1),glass)
        
        if  ((z2-z1)//2)%2==0:
                print(z1+(tailleZ//4))
                poserPorte((x1+tailleX//2,hauteurMin+1,z1+(tailleZ//4)),door_east)
                poserPorte((x1+tailleX//2,hauteurMin+1,z1+(tailleZ//4)-1),door_east)
                mur_sol((x1,y1,z1+(tailleZ//4)-1),(x1+tailleX//2,y1,z1+(tailleZ//4)+1),block_quartz)
                for i in range(tailleX):
                    for j in range(tailleZ):
                        if(z1+j != z1+(tailleZ//4) and z1+j != z1+(tailleZ//4)-1 ) and (x1+i< x1+(tailleX//2) and z1+j<z1+(tailleZ//2)) and(x1+i==x1 or z1+j==z1) and (z1+j != z1+(tailleZ//4) or z1+j != z1+(tailleZ//4)-1) :
                           
                            editor.placeBlock((x1+i,y1+1,z1+j),oak_fence)
                
        else:
             
                poserPorte((x1+tailleX//2,hauteurMin+1,z1+(tailleX//4)),door_east)
                mur_sol((x1,y1,z1+(tailleZ//4)),(x1+tailleX//2,y1,z1+(tailleZ//4)+1),block_quartz)
                for i in range(tailleX):
                    for j in range(tailleZ):
                        if (x1+i< x1+(tailleX//2) and z1+j<z1+(tailleZ//2)) and(x1+i==x1 or z1+j==z1) and z1+j != z1+(tailleZ//4):
                            
                            editor.placeBlock((x1+i,y1+1,z1+j),oak_fence)
                
                
        poserToit(co1,co2,hauteurMax,cotegarage)    
        
       
    
    
    elif cotegarage=='left':
            
        
                            
                    
                                
                
              
               
                        
                    
                                
        
        
        #murs
        poserGarage((x1+1,y1+1,z1+1),(x1+1,y1+3,midtailleZ-1))
        mur_sol((x1,y1+1,z1),(x2,y1+5,z1),block_white_concrete)
        mur_sol((x1,y1+1,z1),(x1,y1+5,midtailleZ   ),block_white_concrete)
        mur_sol((x2-1,y1+1,z1),(x2-1,y1+5,z2),block_white_concrete)
        mur_sol((x1,y1+1,midtailleZ-1),(midtailleX+1,y1+5,midtailleZ-1),block_white_concrete)
        mur_sol((midtailleX,y1+1,midtailleZ),(midtailleX,y1+5,z2),block_white_concrete)
        mur_sol((midtailleX,y1+1,z2-1),(x2,y1+5,z2-1),block_white_concrete)
        
        
        mur_sol((x1,y1+1,z1+1),(x1,y1+4,midtailleZ-1),air)
        
        #sols/plafonds
        mur_sol((x1,y1+4,z1),(x2,y1+4,midtailleZ),block_white_concrete)
        mur_sol((x1,y1,z1),(x2,y1,midtailleZ),oak_planks)
        mur_sol((midtailleX,y1+4,midtailleZ),(x2,y1+4,z2),block_white_concrete)
        mur_sol((midtailleX,y1,midtailleZ),(x2,y1,z2),oak_planks)
        mur_sol((x1,y1,midtailleZ),(midtailleX,y1,z2),grass_block)
        
        poserFenetre((midtailleX,y1+1,midtailleZ+1),(midtailleX,y1+5,z2-1),glass)
        poserFenetre((x2-1,y1+1,z1+1),(x2-1,y1+5,z2-1),glass)
        poserFenetre((midtailleX+1,y1+1,z2-1),(x2-1,y1+5,z2-1),glass)
        poserFenetre((x1+2,y1+1,z1),(x2-1,y1+5,z1),glass)
        poserFenetre((x1+2,y1+1,midtailleZ-1),(midtailleX-1,y1+5,midtailleZ-1),glass)
        
        
        
      
        if  (tailleZ-((z2-z1)//2))%2==0:
    
                poserPorte((x1+tailleX//2,hauteurMin+1,z2-(tailleZ//4)-2),door_east)
                poserPorte((x1+tailleX//2,hauteurMin+1,z2-(tailleZ//4)-1),door_east)
                mur_sol((x1,y1,z2-(tailleZ//4)-2),(x1+tailleX//2,y1,z2-(tailleZ//4)),block_quartz)
                for i in range(tailleX):
                    for j in range(tailleZ):
                        if (x1+i< x1+(tailleX//2) and z2-j>z2-tailleZ//2 ) and(x1+i==x1 or z2-j==z2) and z2-j != z2-(tailleZ//4)-1 and z2-j != z2-(tailleZ//4):
                            
                            editor.placeBlock((x1+i,y1+1,z2-1-j),oak_fence)
        else:
             
                poserPorte((x1+tailleX//2,hauteurMin+1,z2-(tailleZ//4)-1),door_east)
                mur_sol((x1,y1,z2-(tailleZ//4)-1),(x1+tailleX//2,y1,z2-(tailleZ//4)),block_quartz)
                for i in range(tailleX):
                    for j in range(tailleZ):
                        if (x1+i< x1+(tailleX//2) and z2-j>z2-tailleZ//2 ) and (x1+i==x1 or z2-j==z2) and z2-j != z2-(tailleZ//4):
                            print(1)
                            editor.placeBlock((x1+i,y1+1,z2-1-j),oak_fence)
                          
                
                
                
        poserToit(co1,co2,hauteurMax,cotegarage)    
        
        
        
    
    print('Done')
    
    
if __name__=="__main__":
    
    delete((-10,-60,-10),(90,-40,130)) 
    
    house((10,-60,15),(86,-60,124),"left",10)

   
    

    
    
    
    
    
