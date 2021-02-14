class Pokemon:
    def __init__(self, name, attack, level, HP=20):
        self.name = name
        self.attack = attack
        self.level = level
        self.HP = HP

    def fight(self, other):
        return f"{self.name} used {self.attack} on {other.name}!"



    

def lvlUP(self):
    self.level += 1
    self.HP += 2


pkmn1 = Pokemon('Charmander', 'Ember', 6, 22)


pkmn2 = Pokemon('Bulbasaur', 'Absorb', 7, 24)


print(pkmn1.fight(pkmn2))