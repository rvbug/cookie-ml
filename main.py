#!/usr/bin/env python3

import os
import yaml
import argparse
import venv


def parse_args():
    """
    Parses command-line arguments using argparse.

    Returns:
        argparse.Namespace: An object containing parsed arguments.
    """
    # attach arg specs to the parser
    parser = argparse.ArgumentParser(
        prog='ML Cookie Cutter',
        description="Creates ML project cookie cutter structure",
        epilog="Enjoy and happy coding")

    parser.add_argument("--n", "--name", type=str,
                        help="Name of the directory to be created, default = ml-cookie-project", required=False)
    parser.add_argument("--p", "--path", help="provide the path where, default is $HOME dir")
    parser.add_argument("--c", "--config", help="specify your own config file", required=False)
    parser.add_argument("--v", "--venv", action="store_true", help="create a virtual env. "
                                                                   "[ignore if you are already on a virtual env]",
                        required=False)
    # parser.add_argument("--rust", help="support rust structure for ML development in rust")
    return parser.parse_args()


def load_config(config_file="./config.yaml"):
    """
        Loads a configuration from a YAML file.

        Args:
            config_file (str, optional): Path to the configuration file. Defaults to "./config.yaml".

        Returns:
            dict: The parsed configuration dictionary.

        Raises:
            FileNotFoundError: If the specified configuration file is not found.
        """

    # check if the file is provided by the user if it exists
    if not os.path.exists(config_file):
        raise FileNotFoundError(f"f config file not found :{config_file}")
        # we will load the file it exists or else default is config.yaml
    with open(config_file, "r") as f:
        return yaml.safe_load(f)


def create_virtual_env(project_path, activate=True):
    """
    Creates a virtual environment within the specified project directory.

    Args:
        project_path (str): The root path of the project.
        activate (bool, optional): True to print activation instructions, False otherwise. Defaults to True.
    """
    venv_path = os.path.join(project_path, "venv")
    print("virtual env path is ", venv_path)
    if not os.path.exists(venv_path):
        venv.create(venv_path, with_pip=True)
        print("virtual env created at ", venv_path)
        print("you can activate using the following command")
        print(f"source {venv_path}/bin/activate")


def create_directories(project_path, config):
    """
        Creates directories and files based on the provided configuration.

        Args:
            project_path (str): The root path for the project directory.
            config (str, list, or dict): The configuration structure for directories and files.
        """

    if isinstance(config, str):
        item_path = os.path.join(project_path, config)
        with open(item_path, "w"):
            pass  # empty file
    elif isinstance(config, list):
        for item in config:
            create_directories(project_path, item)
    elif isinstance(config, dict):
        for key, value in config.items():
            if key == "files":
                for file in value:
                    file_path = os.path.join(project_path, file)
                    with open(file_path, "w"):
                        pass
            else:
                sub_items = os.path.join(project_path, key)
                os.makedirs(sub_items, exist_ok=True)
                create_directories(sub_items, value)


def main():
    # parse the arguments provided on the command line
    args = parse_args()

    # config = load_config() if args.c is None else load_config(args.c)
    config = load_config()
    # either project name is in the argument or default as "ml-cookie-cuter
    project_name = args.n or "ml-cookie-cutter"
    project_path = args.p or os.environ["HOME"]

    project_path = os.path.join(project_path, project_name) if project_path else project_name

    # # all print stuff here for debugging
    # print("args is ", args)
    # print("project name is ", project_name)
    # print("project_path is ", project_path)
    # print("config is ", config)

    create_directories(project_path, config)
    print("ML directory structure created at :- ", project_path)
    # create venv if user requests it
    if args.v:
        create_virtual_env(project_path)


if __name__ == "__main__":
    main()
