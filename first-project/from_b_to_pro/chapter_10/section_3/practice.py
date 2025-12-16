# 10.6
from pathlib import Path


def sum():
    print("Please enter two number, we will give you sum of them.")

    first_number = input(f"\nPlease enter the first number:")
    second_number = input(f"\nPlease enter the second number:")
    try:
        anwser = int(first_number) + int(second_number)
    except ValueError:
        print("\nPlease provide a valid number.")
    else:
        print(f"\nThe sum of two numbers is：{anwser}")


# 10.7


def sum_while():
    print("Please enter two number, we will give you sum of them.")
    flag = True
    flag_two = True
    while flag:
        try:
            first_number = input(f"\nPlease enter the first number:")
            int(first_number)
        except ValueError:
            print("\nPlease provide a valid number, try again...")
        else:
            flag = False
    while flag_two:
        try:
            second_number = input(f"\nPlease enter the second number:")
            int(second_number)
        except ValueError:
            print("\nPlease provide a valid number, try again...")
        else:
            flag_two = False
    answer = int(first_number) + int(second_number)
    print(f"\nThe sum of two numbers is：{answer}")


# 10.8


def catch_animals(path):
    try:
        contents = path.read_text()
    except FileNotFoundError:
        print(f"The file {path} does not exist!")
    else:
        animals = contents.split()
        for animal in animals:
            print(animal)


# 10.9
def catch_animals_mute(path):
    try:
        contents = path.read_text()
    except FileNotFoundError:
        pass
    else:
        animals = contents.split()
        for animal in animals:
            print(animal)


# 10.10
def count_number(path):
    path_abs = Path(__file__).parent / path
    try:
        contents = path_abs.read_text(encoding="utf-8")
    except FileNotFoundError:
        pass
    else:
        count = contents.lower().count("the ")
        print(f'The word "the" has appeared {count} times in {path}')


count_number("pg11.txt")
