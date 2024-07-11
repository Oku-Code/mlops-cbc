import json
from pathlib import Path

FILE = Path("data.json")

data = {
    'name': 'JD Rodas Barco',
    'age': 29,
    'ocupations': ["MLOps", "DevOps", "Linux"],
    'hobbies': ["Fighting game enthusiast", "Reader"]
}

try:
    with FILE.open('r') as file:
        contents = file.readlines()
        for line in contents:
            print(line)
except FileNotFoundError:
    print("File not in path...")

