#!/usr/bin/env python3

import os
import yaml
import argparse


def create_directories(config_file, project_name):
    with open(config_file, "r") as file:
        config = yaml.safe_load(file)
        print(config)   
        # use user given path or default to $HOME folder 
        project_dir = os.path.join(os.path.expanduser("~"), project_name) 
        print(project_dir)


def main():
    print("calling main function")

if __name__ == "__main__":
    config_file = "config1.yaml"

    # attach arg specs to the parser
    parser = argparse.ArgumentParser(
        prog='ML Cookie Cutter',
        description="Creates ML project cookie cutter structure")
        #epilog="Enjoy and happy coding")
        
    # action = how argument should be handled
    parser.add_argument("--help", "--h", help="show this help message and exit")
    parser.add_argument("--project", "--p", 
                        help="Name of the project to be created, default is ml-cookie-project" )
    parser.add_argument("--config", "-c", help="specify your own config file")
    args = parser.parse_args()
    #print(args.accumulate(args.help))


    #create_directories(config_file, "cookie_ml_testing")
    main() 
