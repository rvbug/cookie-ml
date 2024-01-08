#!/usr/bin/env python3
import os
import yaml


def get_config_file(config_file):
    """
    loads the config.yaml file safely
    why yaml file: you can customize the structure the way you want
    """
    with open(config_file, 'r') as f:
        return yaml.safe_load(f)


def create_directory(directory):
    """
    This will create the directory as listed in the yaml file
    """
    for dir in directory:
        try:
            os.makedirs(dir)
            print(f"directory {dir} created")
        except OSError as e:
            print(e)
            # if e.errno != os.errno.EEXIST:
            # raise  # Re-raise exception
            print(f"Directory '{directory}' already exists.")


if __name__ == "__main__":

    config_file = 'config.yaml'
    directory = create_directory(config_file).get('directory', [])

    if not directory:
        print("seems to be an error in the yaml file, check again!")
    else:
        print("folder structure created.. happy coding!!")

