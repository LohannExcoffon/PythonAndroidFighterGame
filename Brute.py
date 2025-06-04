import random
import json

class Brute:
    def __init__(self, name):
        """
        Initializes a new Brute with randomized base stats and default attributes.
        
        Parameters:
            name: str - The name chosen for the Brute being initialized
        """
        
        # The name of the Brute.
        self.name = name
        
        # Level of the Brute. Initialized at level 1
        self.level = 1
        
        # Total XP earned across all levels
        self.total_xp = 0
        
        # Current XP toward the next level
        self.xp = 0
        
        # XP required to reach the next level
        self.xp_to_level = 10
        
        # Maximum health points. Initialized as random int
        self.max_hp = random.randint(50, 65)
        
        # Current health points. To be changed during a fight. Initially maxed.
        self.current_hp = self.max_hp
        
        # Number of fights won
        self.wins = 0
        
        # Number of fights lost
        self.losses = 0
        
        # Dictionary storing win counts versus specific opponents
        self.winPerBrute = {}
    
        # List of weapons held by the Brute
        self.weapons = []
        
        def generate_balanced_stats():
            """
            Generates a set of the three combat stats (strength, agility, speed).
            
            Returns:
                list[int]: A list of three integers representing [strength, agility, speed]
            """
            while True:
                stats = [
                    random.randint(5, 10),
                    random.randint(5, 10),
                    random.randint(5, 10)
                ]
                total = sum(stats)
                if 20 <= total <= 22:
                    return stats

        # Base Brute statistics. Initially randomized within a range. 
        self.strength, self.agility, self.speed = generate_balanced_stats()
    
        
    def is_alive(self):
        """
        Returns whether the Brute is still alive.

        Returns:
            bool: True if current HP is greater than zero, else False
        """
        return self.current_hp > 0

    def __str__(self):
        """
        Returns a string summary of the Brute's stats and status.

        Returns:
            str: A string showing name, level, HP, strength, agility, and speed
        """
        return f"{self.name} (Lv{self.level}) [HP: {self.current_hp}/{self.max_hp}, STR: {self.strength}, AGI: {self.agility}, SPD: {self.speed}]"
    
    def gain_xp(self, amount):
        """
        Increases the Brute's XP by the given amount and handles leveling up if needed

        Parameters:
            amount: int - Amount of XP to add
        """
        self.total_xp += amount
        self.xp += amount
        self.xp_to_level -= amount
        print(f"{self.name} gains {amount} XP")
        if self.xp_to_level <= 0:
            self.level_up()
        else:
            print(f"{self.xp_to_level} XP needed to level up")
            
            
    def level_up(self):
        """
        Levels up the Brute and increase statistics.

        - Increases level by 1.
        - Recalculates XP needed for the next level.
        - Randomly increases max HP, strength, agility, and speed.
        - Restores current HP to new max HP.
        """
        self.level += 1
        self.xp_to_level = int(self.xp * 1.5)
        self.xp = 0
        print(f"{self.name} leveled up to level {self.level}!")

        # Increase stats
        hp_gain = random.randint(4, 6)
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
        """
        Serializes the Brute object into a dictionary for JSON storage.

        Returns:
            dict: A dictionary representation of the Brute's state
        """
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
            'wins': self.wins,
            'losses': self.losses,
            'winPerBrute': self.winPerBrute,
            'weapons': self.weapons,
        }

    @staticmethod
    def from_dict(data):
        """
        Creates a Brute instance from a dictionary

        Parameters:
            data: dict - A dictionary containing Brute attributes

        Returns:
            Brute: A Brute object with attributes loaded from the dictionary
        """
        b = Brute(data['name'])
        b.level = data['level']
        b.xp = data['xp']
        b.xp_to_level = data['xp_to_level']
        b.max_hp = data['max_hp']
        b.current_hp = data['current_hp']
        b.strength = data['strength']
        b.agility = data['agility']
        b.speed = data['speed']
        b.wins = data['wins']
        b.losses = data['losses']
        b.winPerBrute = data['winPerBrute']
        b.weapons = data['weapons']
        return b
