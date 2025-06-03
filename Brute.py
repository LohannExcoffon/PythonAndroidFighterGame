import random
import json

class Brute:
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.total_xp = 0
        self.xp = 0
        self.xp_to_level = 10
        self.max_hp = random.randint(80, 120)
        self.current_hp = self.max_hp
        self.strength = random.randint(5, 15)
        self.agility = random.randint(5, 15)
        self.speed = random.randint(5, 15)
        self.weapons = []

    def is_alive(self):
        return self.current_hp > 0

    def __str__(self):
        return f"{self.name} (Lv{self.level}) [HP: {self.current_hp}/{self.max_hp}, STR: {self.strength}, AGI: {self.agility}, SPD: {self.speed}]"
    
    def gain_xp(self, amount):
        self.total_xp += amount
        self.xp += amount
        self.xp_to_level -= amount
        print(f"{self.name} gains {amount} XP")
        if self.xp_to_level <= 0:
            self.level_up()
        else:
            print(f"{self.xp_to_level} XP needed to level up")
            
            
    def level_up(self):
        self.level += 1
        self.xp_to_level = int(self.xp * 1.5)
        self.xp = 0
        print(f"{self.name} leveled up to Lv{self.level}!")

        # Increase stats
        hp_gain = random.randint(10, 20)
        str_gain = random.randint(1, 3)
        agi_gain = random.randint(1, 3)
        spd_gain = random.randint(1, 3)

        self.max_hp += hp_gain
        self.current_hp = self.max_hp
        self.strength += str_gain
        self.agility += agi_gain
        self.speed += spd_gain

        print(f"{self.name}'s stats increased! +{hp_gain} HP, +{str_gain} STR, +{agi_gain} AGI, +{spd_gain} SPD")
        
    def to_dict(self):
        return {
            'name': self.name,
            'level': self.level,
            'xp': self.xp,
            'xp_to_level': self.xp_to_level,
            'max_hp': self.max_hp,
            'current_hp': self.current_hp,
            'strength': self.strength,
            'agility': self.agility,
            'speed': self.speed,
            'weapons': self.weapons,
        }

    @staticmethod
    def from_dict(data):
        b = Brute(data['name'])
        b.level = data['level']
        b.xp = data['xp']
        b.xp_to_level = data['xp_to_level']
        b.max_hp = data['max_hp']
        b.current_hp = data['current_hp']
        b.strength = data['strength']
        b.agility = data['agility']
        b.speed = data['speed']
        b.weapons = data['weapons']
        return b
