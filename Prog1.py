import random

def deplacer_robot(tableau_size):
    # Position de départ du robot
    position = (0, 0)
    deplacements = 0

    while True:
        # Incrémente le compteur de déplacements
        deplacements += 1
        
        # Choisir une direction aléatoire
        direction = random.choice(['haut', 'bas', 'gauche', 'droite'])

        # Met à jour la position en fonction de la direction choisie
        if direction == 'haut':
            position = (max(0, position[0] - 1), position[1])
        elif direction == 'bas':
            position = (min(tableau_size[0] - 1, position[0] + 1), position[1])
        elif direction == 'gauche':
            position = (position[0], max(0, position[1] - 1))
        elif direction == 'droite':
            position = (position[0], min(tableau_size[1] - 1, position[1] + 1))

        # Vérifie si le robot a gagné
        if position[0] == tableau_size[0] - 1 or position[1] == tableau_size[1] - 1:
            break

    return deplacements

def simuler_robot(n, tableau_size):
    total_deplacements = 0

    for _ in range(n):
        total_deplacements += deplacer_robot(tableau_size)

    moyenne_deplacements = total_deplacements / n
    return moyenne_deplacements

# Paramètres
n = 100  # Nombre de simulations
tableau_size = (5, 5)  # Taille du tableau

# Exécution de la simulation
moyenne = simuler_robot(n, tableau_size)
print(f'Moyenne des déplacements nécessaires : {moyenne}')