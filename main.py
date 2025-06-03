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
        base_damage = attacker.strength + random.randint(0, 5)
        defender.current_hp -= base_damage
        print(f"{attacker.name} dealt {base_damage} damage")
        
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


brute_a = load_brute('Alex.json')
brute_b = load_brute('Steve.json')
brute_a = generate_random_brute("Alex")
brute_b = generate_random_brute("Steve")

simulate_fight(brute_a, brute_b)

save_brute(brute_a, f"{brute_a.name}.json")
save_brute(brute_b, f"{brute_b.name}.json")
