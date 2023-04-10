# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 08:16:15 2022

@author: Josué
"""


#                   déclaration
L1 = [];
L2 = [];

list_machine1 = [[], []];
list_machine2 = [[], []];

list_final_tache = [];
list_final_ordre = [];

#                   affichage
print ("Bonjour tout le monde !n");
nombre_de_tache = int(input("Combien il y a de tâches ? "));

i = 0;
while i < nombre_de_tache :
#                   remplie les durées pour les deux machines
    print("Pour la tâche",i+1,",");
    duree_courante = int(input("Quelle est le temps de la machine 1 ? "));
    list_machine1[0].append(duree_courante);
    duree_courante = int(input("Quelle est le temps de la machine 2 ? "));
    list_machine2[0].append(duree_courante);
    i = i+1;
    
j = 0;
while j < nombre_de_tache :
#                   remplie les tâches
    list_final_tache.append(j+1);
    list_machine1[1].append(j+1);
    list_machine2[1].append(j+1);
    j = j +1

#                   liste de travail
W = list_machine1[0] + list_machine2[0];

while W != []:
#                   cherche le minimum
    minimum = min(W);
    if (minimum in list_machine1[0]) :
        index = list_machine1[0].index(minimum);
#                   garde en mémoire la tâche
        L1.append(list_machine1[1][index]);
#                   supprime
        del list_machine1[0][index];
        del list_machine2[0][index];
        del list_machine1[1][index];1
        del list_machine2[1][index];
#                   nouvelle liste de travail
        W = list_machine1[0] + list_machine2[0];
    else :
        index = list_machine2[0].index(minimum);
#                   garde en mémoire la tâche
        L2.insert(0, list_machine2[1][index]);
#                   supprime
        del list_machine1[0][index];
        del list_machine2[0][index];
        del list_machine1[1][index];
        del list_machine2[1][index];
#                   nouvelle liste de travail
        W = list_machine1[0] + list_machine2[0];

#                   concaténation
list_final_ordre = L1 + L2;

#                   affichage
print ("n");
print ("tâche : ",list_final_tache);
print ("ordre : ",list_final_ordre);