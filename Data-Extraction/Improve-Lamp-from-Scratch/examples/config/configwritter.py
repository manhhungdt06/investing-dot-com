from configparser import ConfigParser
from pathlib import Path

if __name__ == "__main__":
    current_folder = Path(__file__).parent.resolve()
    config = ConfigParser()

    config["DEFAULT"] = {
        "numberdigits": 4,
        "numbertries": 8,
        "playername": "Hung",
    }

    config["Neural"] = {
        "numberdigits": 6,
        "numbertries": 8,
        "playername": "NeuralLinkNetwork",
    }

    config["SUDO"] = {
        "numberdigits": 5,
        "numbertries": 8,
        "playername": "Cheater",
        "cheats": "on",
    }

    with open(f"{current_folder}/numberguessing.ini", "w") as f:
        config.write(f)
