class Pokemon:
  def __init__(self, name, level, type_, max_health, current_health, is_knocked_out):
    self.name = name
    self.level = level
    self.type_ = type_
    self.max_health = max_health
    self.current_health = current_health
    self.is_knocked_out = is_knocked_out
    

  def lose_health(self, points):
    hp_after_loss = self.current_health - points
    if hp_after_loss <= 0:
      return self.knock_out()
    else:
      print(self.name + " has " + str(hp_after_loss) + " health points left")
      return self.current_health
  

  def gain_health(self, points):
    hp_after_gain = self.current_health + points
    if hp_after_gain >= self.max_health:
      print(self.name + " has maximum health: " + str(self.max_health))
      return self.max_health
    else:
      print(self.name + " now has " + str(hp_after_gain) + " health points")
      return self.current_health


  def knock_out(self):
    if self.current_health <= 0:
      print(self.name + " knocked out")


  def attack(self, other_pokemon):
    poke_dict = {"Fire":0, "Water":2, "Grass":3}
    p1 = poke_dict[self.type_]
    p2 = poke_dict[other_pokemon.type_]
    dif = p1 - p2
    if dif in [-3, 2, 1]:
      damage = self.level*2
    elif dif in [-2, -1, 3]:
      damage = self.level/2
    else:
      damage = self.level
    return other_pokemon.lose_health(damage)


class Trainer(Pokemon):
  def __init__(self, name, pokemon_owned, potions, active_pokemon):
    self.pokemon_owned = pokemon_owned
    self.name = name
    self.potions = potions
    self.active_pokemon = active_pokemon


  def use_potion(self, potion_num):
    self.potions -= potion_num
    print(self.name + " uses potion to heal " + self.active_pokemon.name)
    self.active_pokemon.gain_health(potion_num*3)
    return self.active_pokemon.current_health


  def fight_with(self, other_trainer):
    print(self.name + " uses " + self.active_pokemon.name + " to attack " + other_trainer.active_pokemon.name)
    return self.active_pokemon.attack(other_trainer.active_pokemon)


  def switch_pokemon(self):
    print("You're using " + self.active_pokemon.name + " now.")
    print("Which pokemon would you like to use next?")
    print("1: " + self.pokemon_owned[0].name)
    print("2: " + self.pokemon_owned[1].name)
    print("3: " + self.pokemon_owned[2].name)
    choice = int(input("Click 1, 2 or 3 to make your choice: "))
    self.active_pokemon = self.pokemon_owned[choice-1]
    print(self.active_pokemon.name + " is now active!")


# Pokemons    
charmander = Pokemon("Charmander", 5, "Fire", 100, 100, False)
bulbasaur = Pokemon("Bulbasaur", 7, "Grass", 100, 100, False)
psyduck = Pokemon("Psyduck", 6, "Water", 100, 100, False)
staryu = Pokemon("Staryu", 7, "Water", 100, 100, False)
ponyta = Pokemon("Ponyta", 4, "Fire", 100, 90, False)
oddish = Pokemon("Oddish", 6, "Grass", 100, 100, False)

ash_poke = [charmander, bulbasaur, psyduck]
misty_poke = [staryu, ponyta, oddish]

#Trainers
Ash = Trainer("Ash", ash_poke, 3, ash_poke[1])
Misty = Trainer("Misty", misty_poke, 4, misty_poke[0])
