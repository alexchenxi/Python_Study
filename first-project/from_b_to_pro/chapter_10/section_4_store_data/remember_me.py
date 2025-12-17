import json
from pathlib import Path


def get_stored_username(path):
    if path.exists():
        contents = path.read_text()
        return json.loads(contents)
    else:
        return None


def get_new_username(path):
    username = input("Enter your username: ")

    contents = json.dumps(username)
    path.write_text(contents, encoding="utf-8")
    return username


def greet_user():
    path = Path(__file__).parent / "username.json"
    username = get_stored_username(path)
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = get_new_username(path)
        print(f"We'll remember you when you come back, {username}!")


greet_user()
