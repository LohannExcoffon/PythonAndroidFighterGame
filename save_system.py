import json
import os
from Brute import *


FILEPATH = "brutes.json"

def save_brute(brute, filepath=FILEPATH):
    # Load existing data if it exists
    if os.path.exists(filepath):
        with open(filepath, 'r') as f:
            data = json.load(f)
    else:
        data = []

    # Check if brute with the same name exists
    for i, entry in enumerate(data):
        if entry['name'].lower() == brute.name.lower():
            data[i] = brute.to_dict()
            break
    else:
        data.append(brute.to_dict())

    # Save updated list
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2)

def load_brute(name, filepath=FILEPATH):
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"No file found: {filepath}")
    
    with open(filepath, 'r') as f:
        data = json.load(f)
    
    for entry in data:
        if entry['name'].lower() == name.lower():
            return Brute.from_dict(entry)
    
    raise ValueError(f"Brute named '{name}' not found in {filepath}")
