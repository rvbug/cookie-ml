


[![github](https://img.shields.io/badge/GitHub-rvbug-181717.svg?style=flat&logo=github)](https://github.com/rvbug)
[![twitter](https://img.shields.io/badge/Twitter-@rvbugged-00aced.svg?style=flat&logo=twitter)](https://twitter.com/rvbugged)
[![website](https://img.shields.io/badge/Website-rvbug-5087B2.svg?style=flat&logo=telegram)](https://rvbug.github.io)   
<br><br>
[![python](https://img.shields.io/badge/Python-3.9-3776AB.svg?style=flat&logo=python&logoColor=white)](https://www.python.org)
[![linting: pylint](https://img.shields.io/badge/linting-pylint-yellowgreen)](https://github.com/pylint-dev/pylint)

# Introduction

All ML projects start with basic understanding of data and experiement with Jupyter notebook (mostly) and then gradually moving to a proper IDE, writing/reusing helper functions, seperating data_pipline code with data processing etc. It is chaotic for beginners but that is the beauty of it.


# About this project

Using a standard structure helps you focus on getting started immediately on any machine learning project.   

I tend to start using jupyter notebook to get an understanding of the data, the story it tries to tell, capturing all the details including references, links, tips and tricks, latest researech. These are important information to store during the initial days of your research on the project.




# Project Structure

The project structure is quite simple actually
![image](https://github.com/rvbug/cookie-ml/assets/10928536/e0785d48-c21b-42c6-84a7-de211e6687ca)


# Usage

It contains a simple python script and a configurable folder structure in YAML format.
Extemely simple to use command line script.

```python
python3 main.py --h

# usage: ML Cookie Cutter [-h] [--n N] [--p P] [--c C] [--v]

# Creates ML project cookie cutter structure

#optional arguments:
#  -h, --help         show this help message and exit
#  --n N, --name N    Name of the directory to be created, default = ml-cookie-project
#  --p P, --path P    provide the path where, default is $HOME dir
#  --v, --venv        create a virtual env. [ignore if you are already on a virtual env]

# Enjoy and happy coding

## Arguments 

```
| short format | long format | description |
| --- | --- | --- |
| --h | --help | displays help |
| --n | --name | (optional) provide project name, defaults to "ml-cookie-cutter"  |
| --p | --path | (optional) provide project location, defaults to $HOME directory |
| --v | --venv | (optional) create virtual env. <br>Activate using `source {venv_path}/bin/activate` |


# Future
- setup tools
- Support for Rust  




# Reference 
- [Real Python](https://realpython.com/)  
- [Virtual Env](https://docs.python.org/3/library/venv.html)
- [YAML](https://yaml.org/)  
- [Data Version Control](https://dvc.org/)    
- [Dags Hub](https://dagshub.com/)  
- [Jupyter Notebook](https://jupyter.org/)  
- [Docker](https://www.docker.com/)  
  
  
