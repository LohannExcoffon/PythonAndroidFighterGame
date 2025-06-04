import random
import os
import json
from Brute import Brute
from save_system import load_brute
from save_system import save_brute

FILEPATH = "brutes.json"

def generate_random_brute(name):
    """
    Create a new Brute instance with randomized base stats that add up to ~30.

    The Brute is initialized with:
    - Randomized HP, strength, agility, and speed
    - Default level, XP, and no weapons or skills
    - The given name

    Parameters:
        name: str - The unique name of the Brute to create

    Returns:
        Brute: A new Brute object
    """
    
    # Check for uniqueness of inputted name
    if os.path.exists(FILEPATH):
        with open(FILEPATH, 'r') as f:
            existing_data = json.load(f)
        for entry in existing_data:
            if entry['name'].lower() == name.lower():
                print(f"Brute name '{name}' is already taken.")
                return None
            
    brute = Brute(name)
    return brute

def updateRivalry(winner, loser):
    if loser.name in winner.winPerBrute:
        winner.winPerBrute[loser.name] += 1
    else:
        loser.winPerBrute[winner.name] = 0
        winner.winPerBrute[loser.name] = 1
        
def printRivalry(brute1,brute2):
    if brute2.name in brute1.winPerBrute:
        print(f"You have a rivalry of {brute1.winPerBrute[brute2.name]}W - {brute2.winPerBrute[brute1.name]}L against {brute2.name}")
    else:
        print(f"You have a rivalry of 0W - 0L against {brute2.name}")

def simulate_fight(brute1, brute2):
    printRivalry(brute1,brute2)
    print("FIGHT START!")
    print(brute1)
    print(brute2)
    print()

    # Decide first attacker
    if brute1.speed > brute2.speed:
        attacker, defender = brute1, brute2
    else:
        attacker, defender = brute2, brute1

    turn = 1
    while brute1.is_alive() and brute2.is_alive():
        print(f"Turn {turn}: {attacker.name} attacks {defender.name}")
        base_damage = attacker.strength + random.randint(0, int(attacker.strength / 5))
        defender.current_hp -= base_damage
        print(f"{attacker.name} dealt {base_damage} damage")
        
        # Agility difference based extra turn logic
        agi_diff = attacker.agility - defender.agility
        if agi_diff > 0:
            chance = min(0.25, agi_diff * 0.02)
        else:
            chance = random.randint(2,6)/100  # lower chance, max ~5%
        print(chance)
        if random.random() < chance:
            print(f"{attacker.name} gets a bonus strike!")
            continue  # attacker goes again
        
        # Swap attacker/defender
        attacker, defender = defender, attacker
        turn += 1

    winner = brute1 if brute1.is_alive() else brute2
    loser = brute2 if winner == brute1 else brute1
    brute1.current_hp = brute1.max_hp
    brute2.current_hp = brute2.max_hp
    winner.wins += 1
    loser.losses += 1
    updateRivalry(winner, loser)
    winner.gain_xp(int((loser.level / winner.level) * 10))
    loser.gain_xp(3)
    print(f"\n🏆 {winner.name} wins the battle!")


try:
    brute_a = load_brute("Steve")
except:
    brute_a = generate_random_brute("Steve")

try:
    brute_b = load_brute("Alex")
except:
    brute_b = generate_random_brute("Alex")

simulate_fight(brute_a, brute_b)

save_brute(brute_a)
save_brute(brute_b)
