import json

data = {
    'name': 'JD Rodas Barco',
    'age': 29,
    'ocupations': ["MLOps", "DevOps", "Linux"],
    'hobbies': ["Fighting game enthusiast", "Reader"]
}

try:
    with open("data.json", 'a') as file:
        json.dump(data, file)
except FileNotFoundError:
    print("File not in path...")

