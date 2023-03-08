#Indiquer endroit ou se trouve transactions
'''
format fichier : RaisonEnAttaché Payeur Somme Beneficaire1 Beneficiaire2 Beneficiaire3
'''
print("#######################################################################")
FileNameTransactions = input("Ou se trouve le fichier transactions.txt ? (Lien du fichier complet .txt) : " )
print("#######################################################################")
''' Hardcodé : FileNameTransactions = transactions.txt
'''
#Ouvrir ledit fichier
with open(FileNameTransactions, 'r') as file:
    transactions = file.readlines()

#créer dictionnaire pour garder balance / benef / solde
percu = {}
balance = {}
solde = {}

for line in transactions:
    # Split the line à l'espace
    mots = line.split()
    #indice 1 = mec qui paye
    spender = mots[1]
    #indice 3 = valeur transac 
    valeur_transaction = mots[3]
    #tracker depense dans dico
    if spender in balance :
        balance[spender] =  (float(balance[spender]) + float(valeur_transaction))
    else:
        balance[spender] =  float(valeur_transaction)
    #beneficiaire (ceux qui ont reçu)
    beneficiaires = mots[5:]
    for rat in beneficiaires:
        if rat in percu:
            percu[rat] = float(percu[rat]) + (float(valeur_transaction) / len(beneficiaires))
        else:
            percu[rat] = float(valeur_transaction) / len(beneficiaires)

#Test BugFix : Bug se produit si Nom est présent dans percu mais pas dans balance###
for personne in percu:
    if personne not in balance:
        balance[personne] = 0
####################################################

#difference entre montant perçu et montant payer => solde
for personne in balance:
    x = percu.get(personne, 0) - balance[personne]
    solde [personne] = -x

print("Voici les sommes totales à envoyer / recevoir ")
# Afficher les soldes, arrondi à 2 chiffres apres virgule
for personne, somme in solde.items():
    if somme >= 0:
        print(personne, "doit recevoir : ", round(somme,2))
    else:
        print(personne, "doit envoyer : " , round(somme,2))
print("#######################################################################")
print("Voici la résolution des dettes : ")
#Resoudre les dettes        
while True:
    # Trouver le plus crediteur / endettes
    PlusGrosCrediteur = None
    PlusGrosDebiteur = None
    
    for personne, somme in solde.items():
        if somme < 0:
            if not PlusGrosDebiteur or solde[PlusGrosDebiteur] < somme:
                PlusGrosDebiteur = personne
        elif somme > 0:
            if not PlusGrosCrediteur or solde[PlusGrosCrediteur] > somme:
                PlusGrosCrediteur = personne
    
    # Casser boucle si clefs disparait (== plus de dettes)
    if PlusGrosDebiteur == None or PlusGrosCrediteur == None:
        break
    
    # Calculer somme à transférer
    amount = min(-solde[PlusGrosDebiteur], solde[PlusGrosCrediteur])
    
    # Mettre PlusGrosCrediteur jour la balance + la solde
    balance[PlusGrosDebiteur] += amount
    balance[PlusGrosCrediteur] -= amount
    solde[PlusGrosDebiteur] += amount
    solde[PlusGrosCrediteur] -= amount
    # Afficher les transfers
    print(str(PlusGrosDebiteur) + " paye " + str(PlusGrosCrediteur) + " : " + str(round(amount,2)))
print("#######################################################################")
