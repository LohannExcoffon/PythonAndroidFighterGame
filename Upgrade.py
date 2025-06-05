import random

class Upgrade:
    def __init__(self, strength=0, agility=0, speed=0, health=0, name=None):
        """
        Represents a stat-based upgrade option for a Brute.

        Parameters:
            strength (int): Amount to increase strength.
            agility (int): Amount to increase agility.
            speed (int): Amount to increase speed.
            health (int): Amount to increase max HP.
            rarity (str): One of 'common', 'uncommon', or 'rare'.
            name (str, optional): Custom name for the upgrade. If None, one is auto-generated.
        """
        self.strength = strength
        self.agility = agility
        self.speed = speed
        self.health = health
        self.name = name or self._generate_name()

    def _generate_name(self):
        parts = []
        if self.strength: parts.append(f"+{self.strength} STR")
        if self.agility: parts.append(f"+{self.agility} AGI")
        if self.speed: parts.append(f"+{self.speed} SPD")
        if self.health: parts.append(f"+{self.health} HP")
        return ", ".join(parts) if parts else "No Effect"

    def apply(self, brute):
        """
        Applies this upgrade to the given Brute object.

        Parameters:
            brute (Brute): The Brute receiving the upgrade.
        """
        brute.strength += self.strength
        brute.agility += self.agility
        brute.speed += self.speed
        brute.max_hp += self.health
        brute.current_hp = brute.max_hp  # heal fully on level-up
        print(f"🛠️  {brute.name} gains: {self.name}")

    def __str__(self):
        return f"{self.name}"
