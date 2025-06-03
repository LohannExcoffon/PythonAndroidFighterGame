import json
import os
from Brute import Brute

def save_brute(brute, filename):
    with open(filename, 'w') as f:
        json.dump(brute.to_dict(), f, indent=2)
    print(f"Saved {brute.name} to {filename}")

def load_brute(filename):
    if not os.path.exists(filename):
        raise FileNotFoundError(f"No file found: {filename}")
    with open(filename, 'r') as f:
        data = json.load(f)
        return Brute.from_dict(data)
