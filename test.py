#!/usr/bin/env python3

import os
import yaml
import argparse
import venv
import toml


def parse_args():
    # attach arg specs to the parser
    parser = argparse.ArgumentParser(
        prog='ML Cookie Cutter',
        description="Creates ML project cookie cutter structure",
        epilog="Enjoy and happy coding")

    parser.add_argument("--n", "--name", type=str,
                        help="Name of the directory to be created, default = ml-cookie-project", required=False)
    parser.add_argument("--p", "--path", help="provide the path where, default is $HOME dir")
    parser.add_argument("--c", "--config", help="specify your own config file", required=False)
    parser.add_argument("--d", "--dockerfile", help="Use Docker & create DockerFile. [You need to install docker]")
    parser.add_argument("--v", "--venv", action="store_true", help="create a virtual env. "
                                                                   "[ignore if you are already on a virtual env]",
                        required=False)
    parser.add_argument("--rust", help="support rust structure for ML development in rust")
    return parser.parse_args()


def load_config(config_file="./config.toml"):
    # check if the file is provided by the user if it exists
    if not os.path.exists(config_file):
        raise FileNotFoundError(f"f config file not found :{config_file}")
        # we will load the file it exists or else default is config.yaml
    with open(config_file, "r") as f:
        return toml.load(f)


def create_virtual_env(project_path, activate=True):
    venv_path = os.path.join(project_path, "venv")
    print("virtual env path is ", venv_path)
    if not os.path.exists(venv_path):
        venv.create(venv_path, with_pip=True)
        print("virtual env created at ", venv_path)
        print("virtual env created at ", venv_path)
        print("you can activate using the following command")
        print(f"source {venv_path}/bin/activate")


def create_directories(project_path, structure):
    for key, value in structure.items():
        if isinstance(value, list):
            # Handle lists as directories
            directory_path = os.path.join(project_path, key)
            os.makedirs(directory_path, exist_ok=True)
            for item in value:
                if isinstance(item, str):
                    file_path = os.path.join(directory_path, item)
                    with open(file_path, "w"):
                        pass  # Create empty file
                else:
                    create_directories(directory_path, item)  # Recursively handle nested structures
        elif isinstance(value, dict):
            # Handle nested TOML tables
            create_directories(project_path, value)


def main():
    # parse the arguments provided on the command line
    args = parse_args()
    # either config file is in the argument or default as "config.yaml"
    config = load_config() if args.c is None else load_config(args.c)

    # either project name is in the argument or default as "ml-cookie-cuter
    project_name = args.n or "ml-cookie-cutter"
    project_path = args.p or os.environ["HOME"]

    project_path = os.path.join(project_path, project_name) if project_path else project_name

    create_directories(project_path, config)

    # # all print stuff here for debugging
    # print("args is ", args)
    # print("project name is ", project_name)
    # print("project_path is ", project_path)
    # print("config is ", config)

    # create venv if user requests it
    if args.v:
        create_virtual_env(project_path)


if __name__ == "__main__":
    main()
