import random


class Pokemon:
  def __init__(self, name, level, type_, max_health, current_health, is_knocked_out):
    self.name = name
    self.level = level
    self.type_ = type_
    self.max_health = max_health
    self.current_health = current_health
    self.is_knocked_out = is_knocked_out

  
  def __str__(self):
    return f"{self.name}\nCurrent health: {self.current_health}\nLevel: {self.level}\nType: {self.type_}"
    

  def lose_health(self, points):
    hp_after_loss = self.current_health - points
    if hp_after_loss <= 0:
      return self.knock_out()
    else:
      self.current_health = hp_after_loss
      print(self.name + " has " + str(hp_after_loss) + " health points left")
  

  def gain_health(self, points):
    hp_after_gain = self.current_health + points
    if hp_after_gain >= self.max_health:
      print(self.name + " has maximum health: " + str(self.max_health))
      self.max_health = 100
    else:
      self.current_health = hp_after_gain
      print(self.name + " now has " + str(hp_after_gain) + " health points")


  def knock_out(self):
    self.is_knocked_out = True
    print(self.name + " is knocked out")


  def attack(self, other_pokemon):
    poke_dict = {"Fire":0, "Water":2, "Grass":3}
    p1 = poke_dict[self.type_]
    p2 = poke_dict[other_pokemon.type_]
    dif = p1 - p2
    if self.is_knocked_out != True:
      if dif in [-3, 2, 1]:
        damage = self.level*2
      elif dif in [-2, -1, 3]:
        damage = self.level/2
      else:
        damage = self.level
      return other_pokemon.lose_health(damage)
    else:
      print(f"{self.name} is knocked out and cannot attack anymore.")


class Trainer(Pokemon):
  def __init__(self, name, pokemon_owned, potions, active_pokemon):
    self.pokemon_owned = pokemon_owned
    self.name = name
    self.potions = potions
    self.active_pokemon = active_pokemon
  

  def __str__(self):
    return "{}\nMy pokemons: {}\nActive pokemon: {}\nNumber of potions: {}".format(self.name, 
    [p.name for p in self.pokemon_owned], self.active_pokemon.name, self.potions)
    
  
  def use_potion(self, potion_num):
    self.potions -= potion_num
    print(self.name + " uses " + str(potion_num) + " potion(s) to heal " + self.active_pokemon.name)
    return self.active_pokemon.gain_health(potion_num*3)


  def fight_with(self, other_trainer):
    print(self.name + " uses " + self.active_pokemon.name + " to attack " + other_trainer.active_pokemon.name)
    self.active_pokemon.attack(other_trainer.active_pokemon)


  def switch_pokemon(self):
    print("You're using " + self.active_pokemon.name + " now.")
    print("Which pokemon would you like to use next?")
    print("1: " + self.pokemon_owned[0].name)
    print("2: " + self.pokemon_owned[1].name)
    print("3: " + self.pokemon_owned[2].name)
    number = int(input("Click 1, 2 or 3 to make your choice: "))
    choice = self.pokemon_owned[number-1] 
    if choice.is_knocked_out != True: 
      self.active_pokemon = choice
      print(self.active_pokemon.name + " is now active!")
    else:
      print("This pokemon is knocked out, you cannot use it")
      self.active_pokemon = self.active_pokemon
      

# Pokemons    
Char = Pokemon("Charmander", 10, "Fire", 100, 52, False)
Bul = Pokemon("Bulbasaur", 14, "Grass", 100, 30, False)
Psy = Pokemon("Psyduck", 12, "Water", 100, 40, False)
Star = Pokemon("Staryu", 8, "Water", 100, 65, False)
Pony = Pokemon("Ponyta", 8, "Fire", 100, 60, False)
Odd = Pokemon("Oddish", 6, "Grass", 100, 80, False)
Heat = Pokemon("Heatmor", 4, "Fire", 100, 100, False)
Squi = Pokemon("Squirtle", 6, "Water", 100, 70, False)
Vic = Pokemon("Victreebel", 5, "Grass", 100, 90, False)

all_poke = [Char, Bul, Psy, Star, Pony, Odd, Heat, Squi, Vic]

p1_poke = random.sample(all_poke, 4)
p2_poke = random.sample(all_poke, 4)
p1_name = input("Hi, Player 1! What is your name: ")
p2_name = input("Player 2, nice to meet you! Give me your name: ")

#Trainers
Player1 = Trainer(p1_name, p1_poke, 5, p1_poke[0])
Player2 = Trainer(p2_name, p2_poke, 5, p2_poke[0])

print(f"{p1_name}, {p2_name}, check out your stats!\n")
print("-"*80)
print(Player1)
print("-"*80)
print(Player2)







