import time
import threading

class Robot:
    def __init__(self, name):
        self.__name = name
        self.__power = False
        self.__current_speed = 0
        self.__battery_level = 0  
        self.__states = ['shutdown', 'running']
        self.__charging = False

    def allumer(self):
        self.__power = True
        print(f"{self.__name} est allumé.")

    def eteindre(self):
        self.__power = False
        self.__current_speed = 0
        print(f"{self.__name} est éteint.")

    def charger(self):
        if self.__charging:
            print(f"{self.__name} est déjà en charge.")
            return
        
        self.__charging = True
        print(f"{self.__name} commence à charger...")
        for i in range(1, 101):  # Niveau de charge
            time.sleep(0.01) # Rapidité de charge
            if self.__battery_level < 100:
                self.__battery_level += 1 # Pas de charge
                print(f"Batterie : {self.__battery_level}%")
        self.__charging = False
        print(f"{self.__name} a terminé la charge à 100%.")

    def definir_vitesse(self, vitesse):
        if self.__power:
            self.__current_speed = vitesse
            print(f"Vitesse de {self.__name} réglée à {self.__current_speed} m/s.")
        else:
            print(f"{self.__name} doit être allumé pour définir la vitesse.")

    def obtenir_vitesse(self):
        return self.__current_speed

    def demarrer_deplacement(self):
        if self.__power and self.__battery_level > 0:
            print(f"{self.__name} commence à se déplacer à {self.__current_speed} m/s.")
        else:
            print(f"{self.__name} doit être allumé et avoir de la batterie pour se déplacer.")

    def arreter_deplacement(self):
        print(f"{self.__name} a arrêté son déplacement.")
        self.__current_speed = 0

    def etat_global(self):
        etat = (
            f"État de {self.__name} :\n"
            f"Allumé : {'Oui' if self.__power else 'Non'}\n"
            f"Batterie : {self.__battery_level}%\n"
            f"Vitesse : {self.__current_speed} m/s\n"
            f"En déplacement : {'Oui' if self.__current_speed > 0 else 'Non'}"
        )
        print("\n")
        print(etat)

# Donner un nom au robot
nom_robot = input("Entrez le nom du robot : ")
mon_robot = Robot(nom_robot)

# Allumer le robot
mon_robot.allumer()

# Charger la batterie
charger_thread = threading.Thread(target=mon_robot.charger)
charger_thread.start()
charger_thread.join()  # Attendre la fin de la charge

# Définir la vitesse
vitesse_robot = int(input("A quelle vitesse doit-il aller (en m/s) ? "))
while True:
    if vitesse_robot > 15:
        print("Ce robot ne peut pas aller aussi vite que le faucon Millenium !")
        vitesse_robot = int(input("A quelle vitesse doit-il aller (en m/s) ? "))
    elif vitesse_robot < 5:
        print("Ce robot peut aller plus vite que ta grand-mère !")
        vitesse_robot = int(input("A quelle vitesse doit-il aller (en m/s) ? "))
    else:
        break  # Sortir de la boucle si la vitesse est acceptable
mon_robot.definir_vitesse(vitesse_robot)

# Démarrer le déplacement
mon_robot.demarrer_deplacement()

# Arrêter le déplacement
mon_robot.arreter_deplacement()

# Afficher l'état global
mon_robot.etat_global()

# Éteindre le robot
mon_robot.eteindre()