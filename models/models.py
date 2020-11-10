import random
from cls.classes import Pokemon, Trainer

# Pokemons
all_poke = [
    Pokemon("Charmander", 10, "Fire", 100, 8, False),
    Pokemon("Bulbasaur", 14, "Grass", 100, 30, False),
    Pokemon("Psyduck", 12, "Water", 100, 40, False),
    Pokemon("Staryu", 8, "Water", 100, 65, False),
    Pokemon("Ponyta", 8, "Fire", 100, 60, False),
    Pokemon("Oddish", 6, "Grass", 100, 80, False),
    Pokemon("Heatmor", 4, "Fire", 100, 100, False),
    Pokemon("Squirtle", 6, "Water", 100, 70, False),
    Pokemon("Victreebel", 5, "Grass", 100, 90, False)
    ]

p1_poke = random.sample(all_poke, 3)
p2_poke = random.sample(all_poke, 3)

#Trainers
Player1 = Trainer("Ash", p1_poke, 5, p1_poke[0])
Player2 = Trainer("Misty", p2_poke, 5, p2_poke[0])