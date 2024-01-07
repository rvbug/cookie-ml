import os
import toml

def create_dir(config_file):
    with open(config_file, "r") as f:
        config = toml.load(f)

    for directory in config["directories"]:
        if isinstance(directory, list):
            parent, subdir = directory
            os.makedirs(os.path.join(parent, subdir), exist_ok=True)
        else:
            os.makedirs(directory, exist_ok=True)
        config = toml.load(f)

if __name__ == "__main__":
    create_dir("config.toml")
