import time
import threading
from Prog2 import Robot  

class Humain:
    def __init__(self, sexe):
        self.__sexe = sexe
        self.__aliments = []

    def manger(self, aliment):
        self.__aliments.append(aliment)
        print(f"Le côté humain a mangé : {aliment}")

    def digerer(self):
        if self.__aliments:
            print("Digestion des aliments :")
            for aliment in self.__aliments:
                print(f"- {aliment}")
            self.__aliments.clear()
            print("Tous les aliments ont été digérés.")
        else:
            print("Rien à digérer.")

class Cyborg(Robot, Humain):
    def __init__(self, name, sexe):
        Robot.__init__(self, name)
        Humain.__init__(self, sexe)

    def etat_global(self):
        Robot.etat_global(self)
        print(f"Sexe : {self._Humain__sexe}")
        print(f"Aliments mangés : {', '.join(self._Humain__aliments) if self._Humain__aliments else 'Aucun'}")

# Utilisation de la classe Cyborg
nom_cyborg = input("Entrez le nom du cyborg : ")
sexe_cyborg = input("Entrez le sexe du cyborg (H/F) : ")

mon_cyborg = Cyborg(nom_cyborg, sexe_cyborg)

# Allumer le cyborg
mon_cyborg.allumer()

# Charger la batterie
charger_thread = threading.Thread(target=mon_cyborg.charger)
charger_thread.start()
charger_thread.join()  # Attendre la fin de la charge
compteur = 0
# Le cyborg mange des aliments
while True:
    aliment = input("Quel aliment le cyborg mange-t-il ? (ou 'fin' pour terminer) ")
    compteur += 1 
    if aliment.lower() == 'fin':
        break
    mon_cyborg.manger(aliment)
    if compteur == 4:
        print("Le cyborg a trop mangé il doit faire caca !")
        break

# Démarrer le déplacement
mon_cyborg.definir_vitesse(10)  # Vous pouvez demander une vitesse ici aussi
mon_cyborg.demarrer_deplacement()

# Arrêter le déplacement
mon_cyborg.arreter_deplacement()

# Afficher l'état global
mon_cyborg.etat_global()

# Digérer les aliments mangés
mon_cyborg.digerer()

# Éteindre le cyborg
mon_cyborg.eteindre()