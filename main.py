import random
from Brute import Brute 
from save_system import save_brute
from save_system import load_brute

def generate_random_brute(name):
    brute = Brute(name)
    return brute


def simulate_fight(brute1, brute2):
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
    winner.gain_xp(10)
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
