# 10.11
import json
from pathlib import Path


def save_favorite_number():
    favorite_number = input("Enter favorite number: ")
    try:
        favorite_number = int(favorite_number)
    except ValueError:
        print('Please enter a number.')
        pass
    else:
        contents = json.dumps(favorite_number)
        path = Path(__file__).resolve().parent / 'favorite_number.json'
        path.write_text(contents)
        print("Your favorite number is now stored in 'favorite_number.json'")


def get_favorite_number():
    path = Path(__file__).resolve().parent / 'favorite_number.json'
    if path.exists():
        contents = path.read_text()
        favorite_number = json.loads(contents)
        print(f"I know your favorite number! It's {favorite_number}")
    else:
        print(f"Sorry I don't know your favorite number!")


get_favorite_number()

