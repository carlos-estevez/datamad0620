
# Soldier

class Soldier:
    def __init__(self, health, strength):
        self.health=health 
        self.strength=strength 
    def attack (self):
        return self.strength 
    def receiveDamage(self,damage):
        self.health -= damage

    pass


# Viking


class Viking(Soldier):
    def __init__(self,name,health,strength):
        super().__init__(health,strength)
        self.name=name
    def receiveDamage(self,damage):
        self.health -=  damage
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"
    def battleCry(self):
        return "Odin Owns You All!"

    pass

# Saxon

class Saxon(Soldier):
    def __init__(self,health,strength):
        super().__init__(health,strength)
    def receiveDamage(self,damage):
        self.health -=  damage
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return "A Saxon has died in combat"
        
    pass

# War
import random

class War:
    def __init__(self):
        self.vikingArmy=[]
        self.saxonArmy=[]
    def addViking(self,viking="Viking"):
        self.vikingArmy.append(self.viking*10)
    def addSaxon(self,saxon="Saxon"):
        self.saxonArmy.append(self.saxon*10)
    def vikingAttack(self):


    def saxonAttack(self):
    
    def showStatus(self):


#### `vikingAttack()` method
