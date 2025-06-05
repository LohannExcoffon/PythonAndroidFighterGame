import json
import os
from Brute import *

FILEPATH = "brutes.json"

def save_brute(brute, filepath=FILEPATH):
    """
    Saves or updates a Brute in the JSON file.
    If a Brute with the same name already exists, it updates that entry. If not, 
    it appends the new Brute to the list. Finally, it writes the updated list 
    back to the file.

    Parameters:
        brute: Brute - The Brute object to be saved or updated
        filepath: str - The path to the JSON file storing all the Brutes
    """
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
    """
    Loads a Brute by name from the shared JSON file.
    If the Brute is not found, ir raises an exception.

    Parameters:
        name: str - The name of the Brute to load
        filepath: str - The path to the JSON file storing all the Brutes

    Returns:
        Brute: The Brute object with the given name

    Raises:
        FileNotFoundError: If the JSON file does not exist
        ValueError: If the given name is not found in the file
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"No file found: {filepath}")
    
    with open(filepath, 'r') as f:
        data = json.load(f)
    
    for entry in data:
        if entry['name'].lower() == name.lower():
            return Brute.from_dict(entry)
    
    raise ValueError(f"Brute named '{name}' not found in {filepath}")
