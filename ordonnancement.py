# Algorithme de johnson en python 3

M1 = [6, 3, 10, 14, 5, 9, 7, 11, 2, 3]
M2 = [1, 5, 4, 6, 10, 6, 9, 8, 6, 1]
M3 = [5, 8, 1, 3, 6, 10, 12, 9, 6, 7]

if len(M1) != len(M2) or len(M1) != len(M3):
    print("Les tailles des tableaux des machines doivent être égales")
    quit()
if len(M1) == 0:
    print("Les tailles ne doivent pas être égales à 0")
    quit()

nombre_commande = len(M1)
MV1 = [None] * nombre_commande  # M1 + M2
MV2 = [None] * nombre_commande  # M2 + M3
for i in range(nombre_commande):
    MV1[i] = M1[i] + M2[i]
    MV2[i] = M2[i] + M3[i]
print("MV1(M1 + M2): %s" % MV1)
print("\nMV2(M2 + M3): %s" % MV2)

# Nous avons maintenant deux tableaux MV1 et MV2 et allons appliquer l'algorithme dde Jonhson sur 2 machines
List1 = []  # Liste qui va contenir les numéros de commande si MV1 a la plus petite durée
List2 = []  # Liste qui va contenir les numéros de commande si MV2 a la plus petite durée
for i in range(nombre_commande):
    valeur_min_mv1 = min(MV1)
    valeur_min_mv2 = min(MV2)
    if valeur_min_mv1 < valeur_min_mv2:
        # cas si le minimum a été retrouvé sur MV1
        numero_commande = MV1.index(valeur_min_mv1)
        List1.append(numero_commande)
    else:
        numero_commande = MV2.index(valeur_min_mv2)
        List2.append(numero_commande)
    # on enlève la commande associée au numéro des tableaux MV1 et MV2 en le remplacant par
    # l'infini comme cela l'algorithme ne le prendra pas en compte dans le calcul d'indice
    MV1[numero_commande] = float('inf')
    MV2[numero_commande] = float('inf')
# La liste 2 doit être renversée, car elle se doit se lire de droite à gauche
# On concatène les listes pour avoir l'ordre des commandes.
List2 = list(reversed(List2))
print("\nList1 Correspondant aux minimums de MV1: %s" % List1)
print("\nList2 Correspondant aux minimums de MV2: %s" % List2)
ordre_des_commandes = List1 + List2
print("\nL'ordre des commandes est: %s" % ordre_des_commandes)

# Calcul de Cmax selon l'ordre des commandes de l'algorithme

# Calcul de la durée de traitement de la M1
M1debut = [None] * nombre_commande
M1fin = [None] * nombre_commande
decalage = 0

for i in range(nombre_commande):
    numero_commande = ordre_des_commandes[i]
    M1debut[i] = decalage
    M1fin[i] = decalage + M1[numero_commande]
    decalage = M1fin[i]
print("\nL'exécution de la machine 1 pour les différente commande débutera %s et se terminera %s" % (M1debut, M1fin))

# Calcul de la durée de M2, il faudra faire attention au décalage qui n'est pas forcément
# à la fin de l'execution de la commande précédente
M2debut = [None] * nombre_commande
M2fin = [None] * nombre_commande
decalage = M1fin[0]  # fin de la premiere commande
for i in range(nombre_commande):
    numero_commande = ordre_des_commandes[i]

    M2debut[i] = decalage
    M2fin[i] = decalage + M2[numero_commande]
    # comme décalage pour la prochaine commande, nous devons choisir le maximum entre le temps à la fin de la
    # tache précedente sur M1 et la fin de la tache actuelle sur M2
    if i < (nombre_commande - 1) and M1fin[i + 1] > M2fin[i]:
        decalage = M1fin[i + 1]
    else:
        decalage = M2fin[i]
print("L'exécution de la machine 2 pour les différente commande débutera %s et se terminera %s" % (M2debut, M2fin))

# On refait le même calcul pour M3 en tenant compte du décalage selon M2
M3debut = [None] * nombre_commande
M3fin = [None] * nombre_commande
decalage = M2fin[0]  # fin de la premiere commande
for i in range(nombre_commande):
    numero_commande = ordre_des_commandes[i]

    M3debut[i] = decalage
    M3fin[i] = decalage + M3[numero_commande]
    # comme décalage pour la prochaine commande, nous devons choisir le maximum entre le temps à la fin de la
    # tache précedente sur M2 et la fin de la tache actuelle sur M3
    if i < (nombre_commande - 1) and M2fin[i + 1] > M3fin[i]:
        decalage = M2fin[i + 1]
    else:
        decalage = M3fin[i]

print("L'exécution de la machine 3 pour les différente commande débutera %s et se terminera %s" % (M3debut, M3fin))

# Le CMAX correspond au dernier élément de la colonne (Liste) M3fin
Cmax = M3fin[-1]
print("\nLa valeur Cmax est %s" % Cmax)

# Méthode de liste  par ordre decroissant


M1 = [6, 3, 10, 14, 5, 9, 7, 11, 2, 3]
M2 = [1, 5, 4, 6, 10, 6, 9, 8, 6, 1]
M3 = [5, 8, 1, 3, 6, 10, 12, 9, 6, 7]

M1.sort(reverse=True)
print("\nLa liste par ordre decroissant est %s" % M1)
M2.sort(reverse=True)
print(M2)
M3.sort(reverse=True)
print(M3)

# Méthdode de liste par ordre croissant

M1.sort(reverse=False)
print(M1)
M2.sort(reverse=False)
print(M2)
M3.sort(reverse=False)
print(M3)

# Méthode de liste par ordre croissant et decroissant avec sorted

M1 = [6, 3, 10, 14, 5, 9, 7, 11, 2, 3]
res = sorted(M1, reverse=False)
res = sorted(M1, reverse=True)
print(res)

M2 = [1, 5, 4, 6, 10, 6, 9, 8, 6, 1]
res = sorted(M2, reverse=False)
res = sorted(M2, reverse=True)
print(res)

from plotly.offline import plot
import plotly.graph_objs as go
import plotly.figure_factory as ff
import plotly.express as px
import numpy as np
import pandas as pd

LK=[10,1,3,9,2,4,5,6,7,8]
df = pd.DataFrame([
    dict(Task="Job10", Start='2009-01-01', Finish='2009-01-04', Resource="M1"),
    dict(Task="Job10", Start='2009-01-04', Finish='2009-01-05', Resource="M2"),
    dict(Task="Job10", Start='2009-01-05', Finish='2009-01-12', Resource="M3"),
    dict(Task="Job2", Start='2009-01-04', Finish='2009-01-07', Resource="M1"),
    dict(Task="Job2", Start='2009-01-07', Finish='2009-01-12', Resource="M2"),
    dict(Task="Job2", Start='2009-01-12', Finish='2009-01-20', Resource="M3"),
    dict(Task="Job9", Start='2009-01-07', Finish='2009-01-09', Resource="M1"),
    dict(Task="Job9", Start='2009-01-12', Finish='2009-01-18', Resource="M2"),
    dict(Task="Job9", Start='2009-01-20', Finish='2009-01-26', Resource="M3"),
    dict(Task="Job5", Start='2009-01-09', Finish='2009-01-14', Resource="M1"),
    dict(Task="Job5", Start='2009-01-18', Finish='2009-01-28', Resource="M2"),
    dict(Task="Job5", Start='2009-01-28', Finish='2009-02-03', Resource="M3"),
    dict(Task="Job6", Start='2009-01-14', Finish='2009-01-23', Resource="M1"),
    dict(Task="Job6", Start='2009-01-28', Finish='2009-02-03', Resource="M2"),
    dict(Task="Job6", Start='2009-02-03', Finish='2009-02-13', Resource="M3"),
    dict(Task="Job7", Start='2009-01-23', Finish='2009-01-30', Resource="M1"),
    dict(Task="Job7", Start='2009-02-03', Finish='2009-02-12', Resource="M2"),
    dict(Task="Job7", Start='2009-02-13', Finish='2009-02-25', Resource="M3"),
    dict(Task="Job8", Start='2009-01-30', Finish='2009-02-10', Resource="M1"),
    dict(Task="Job8", Start='2009-02-12', Finish='2009-02-20', Resource="M2"),
    dict(Task="Job8", Start='2009-02-25', Finish='2009-03-06', Resource="M3"),
    dict(Task="Job4", Start='2009-02-10', Finish='2009-02-24', Resource="M1"),
    dict(Task="Job4", Start='2009-02-24', Finish='2009-03-02', Resource="M2"),
    dict(Task="Job4", Start='2009-03-06', Finish='2009-03-09', Resource="M3"),
    dict(Task="Job1", Start='2009-02-24', Finish='2009-03-02', Resource="M1"),
    dict(Task="Job1", Start='2009-03-02', Finish='2009-03-03', Resource="M2"),
    dict(Task="Job1", Start='2009-03-09', Finish='2009-03-14', Resource="M3"),
    dict(Task="Job3", Start='2009-03-02', Finish='2009-03-12', Resource="M1"),
    dict(Task="Job3", Start='2009-03-12', Finish='2009-03-16', Resource="M2"),
    dict(Task="Job3", Start='2009-03-16', Finish='2009-03-17', Resource="M3")
    ])

fig = px.timeline(df, x_start="Start", x_end="Finish", y="Task", color="Resource")
fig.update_yaxes(autorange="reversed")
