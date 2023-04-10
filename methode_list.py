# -*- coding: utf-8 -*-
"""
hCreated on Tue Oct 11 15:02:29 2022

@author: Josué
"""
# méthode de liste avec la machine virtuelle

mv = 0

mv1  = [7,8,14,20,15,15,16,19,9,4]
mv2  = [6,13,5,9,16,16,21,20,12,8]
   
    
mv1.extend(mv2)

print(mv1)

#ajoute la machine virtuelle 1 dans mv1
mv2.extend(mv1)
print(mv2)

if  mv1:
    print("la liste de tâche t est non vide ")
else: 
   
    print(mv1+mv2)




    

         