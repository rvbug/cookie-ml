import argparse
import os

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("folderName", help="- Provide folder name")

    args = parser.parse_args()

    project_name = args.folderName
    os.chdir('../')
    os.mkdir(project_name)
    os.chdir(f"{project_name}")

    dirs = [
        os.path.join("data", "raw"),
        os.path.join("data", "processed"),
        os.path.join("data", "train"),
        os.path.join("data", "test"),
        "notebook",
        os.path.join("notebook", "data"),
        os.path.join("notebook", "report"),
        os.path.join("notebook", "model"),
        os.path.join("notebook", "research"),
        "models",
        "src" ,
        "docs",
    ]

    files = [
        "README1.md",
        "Makefile",
        "reports",
        "logs",
        "plots",
        "params.yaml",
        ".gitignore",
        "Dockerfile",
        os.path.join("src", "__init__.py"),
        os.path.join("notebook", f"{project_name}_EDA_ML_Experiements.ipynb"),
        os.path.join("notebook", f"{project_name}.ipynb"),
        os.path.join("notebook", "research"+"/"+f"{project_name}_papers.ipynb"),

    ]

    for _dir_ in dirs:
        os.makedirs(_dir_, exist_ok=True)
        pass

    for _file_ in files:
        with open(_file_, "w") as f:
            pass
    print("folder structure created.. happy coding!!")
