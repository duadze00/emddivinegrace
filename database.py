import json

FILE_NAME = "account.json"


def load():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


def save(n):
    with open(FILE_NAME, "w") as file:
        json.dump(n, file, indent=4)
