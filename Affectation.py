from pulp import *

# Définir les données d'entrée
lits = ["Lit1", "Lit2", "Lit3", "Lit4", "Lit5", "Lit6", "Lit7", "Lit8", "Lit9", "Lit10"]
patients = ["Patient1", "Patient2", "Patient3", "Patient4", "Patient5", "Patient6", "Patient7", "Patient8", "Patient9", "Patient10"]
capacité_lit = {"Lit1": 1, "Lit2": 1, "Lit3": 1, "Lit4": 1, "Lit5": 1, "Lit6": 1, "Lit7": 1, "Lit8": 1, "Lit9": 1, "Lit10": 1}
demande_patient = {"Patient1": 1, "Patient2": 1, "Patient3": 1, "Patient4": 1, "Patient5": 1, "Patient6": 1, "Patient7": 1, "Patient8": 1, "Patient9": 1, "Patient10": 1}

# Initialiser le problème d'optimisation
problème = LpProblem("Affectation des lits", LpMinimize)

# Définir les variables de décision
affectation_lit = LpVariable.dicts("Affectation", [(p, l) for p in patients for l in lits], lowBound=0, upBound=1, cat=LpInteger)

# Définir la fonction objectif
problème += lpSum([affectation_lit[(p, l)] for p in patients for l in lits])

# Définir les contraintes
for p in patients:
    problème += lpSum([affectation_lit[(p, l)] for l in lits]) == demande_patient[p]
for l in lits:
    problème += lpSum([affectation_lit[(p, l)] for p in patients]) <= capacité_lit[l]

# Résoudre le problème d'optimisation
status = problème.solve()


# Afficher la solution
for p in patients:
    lit_affecté = False
    for l in lits:
        if value(affectation_lit[(p, l)]) == 1:
            print(f"{p} est affecté au {l}")
            lit_affecté = False
    #if not lit_affecté:
        #print(f"{p} est non affecté")








