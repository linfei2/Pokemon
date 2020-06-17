class Pokemon:
  def __init__(self, name, level, typ, max_health, current_health, is_knocked_out):
    self.name = name
    self.level = level
    self.typ = typ
    self.max_health = max_health
    self.current_health = current_health
    self.is_knocked_out = is_knocked_out
    
  def lose_health(self, points):
    hp_after_loss = self.current_health - points
    if hp_after_loss <= 0:
      return knock_out()
    else:
      return self.name + " has " + str(hp_after_loss) + " health points left"
  
  def gain_health(self, points):
    hp_after_gain = self.current_health + points
    if hp_after_gain >= self.max_health:
      return self.name + " has maximum health: " + str(self.max_health)
    else:
      return self.name + " now has " + str(hp_after_gain) + " health points"
    
  def knock_out(self):
    if self.current_health <= 0:
      return self.name + " knocked out"

  def attack(self, other_pokemon):
    if self.typ == "Fire" and other_pokemon.typ == "Grass":
      damage = self.level * 2
    elif self.typ == "Fire" and other_pokemon.typ == "Water":
      damage = self.level / 2
    elif self.typ == "Water" and other_pokemon.typ == "Fire":
      damage = self.level * 2
    elif self.typ == "Water" and other_pokemon.typ == "Grass":
      damage = self.level / 2
    elif self.typ == "Grass" and other_pokemon.typ == "Water":
      damage = self.level * 2
    elif self.typ == "Grass" and other_pokemon.typ == "Fire":
      damage = self.level / 2
    else:
      damage = self.level
      
    return other_pokemon.lose_health(damage)    
    

# Pokemony    
charmander = Pokemon("Charmander", 5, "Fire", 100, 100, False)
bulbasaur = Pokemon("Bulbasaur", 7, "Grass", 100, 100, False)
psyduck = Pokemon("Psyduck", 6, "Water", 100, 100, False)
    

    
