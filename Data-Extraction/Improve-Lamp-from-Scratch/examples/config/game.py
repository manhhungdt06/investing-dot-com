from configparser import ConfigParser
from pathlib import Path
from random import randint

if __name__ == "__main__":
    current_folder = Path(__file__).parent.resolve()

    config = ConfigParser()
    config.read(f"{current_folder}/numberguessing.ini")

    user = input("What is your name?: ")
    if user == "SUDO":
        password = input("Password: ")
        if password != "12345":
            print("Wrong password!")
            exit(0)
    try:
        config_data = config[user]
    except:
        print("User not found!")
        exit(0)

    number = randint(1, 10**(int(config_data['numberdigits'])))
    maxtries = int(config_data['numbertries'])
    tries = 0
    done = False

    while not done:
        guess = input("Guess: ")
        if guess == "cheat":
            if "cheats" in config_data.keys() and config_data["cheats"] == "on":
                print(f"You won! The number was {number}!")
            else:
                print("You are not allowed to cheat!")
            exit(0)
        else:
            guess = int(guess)
        tries += 1

        if guess == number:
            print(f"You won! The number was {number}!")
            print(f"It took you {tries} tries!")
        else:
            if tries == maxtries:
                print(f"You lost after {tries} tries!")
                print(f"The number was {number}!")
                exit(0)
            else:
                print("Too high!") if guess > number else print("Too low!")
