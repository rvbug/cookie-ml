# Preface

>Currently working on quick guide to **make**, **Makefile** and other tools like virtualenv just enough to quickly get your running at full speed.
I will be sharing it shortly


# Introduction


>You have trained your model using `jupyter notebook` / `vscode` / `pycharm`.   
Getting your code into production is a whole new challenge unlike any other you have done before.    
It is chaotic but that is the beauty of it

# About this project

> Helps you to build a project struture easily and is quite flexible.  
Developed in Python 3, you can use it via make or calling python script  
Most importantly, it is extremely simple to use!

# Approches

There are couple of ways you can use this.

1. make & Makefile  

2. run script directly.


## Approach 1

### Prerequisites
 The prerequisites is to have a virtual environment created. There are 3 ways which can be done
 
 - **`conda`** - easier but works well but only during experimental phase of your project
 - **`virtualenv`** - was popular once and works well with *pip*
 - **`pipenv`** - is the most preferred method as it combines `pip` & `virtualenv`  
  
<br>
          
> Once you activate the virtual env, follow the below steps :-
<br>

*`make`* is a utility and a very popluar for automating the compilation of C/C++ programs and their dependencies.

`make` runs the scripts mentioned in `Makefile`

After you clone this repo, call `make` from command line, by default it will show all the arguments you can use
<p>
<img src="https://github.com/rvbug/cookie-ml/blob/main/make.png">


> To get help use
```python
make help
```          
          
#### The order of execution is as follows :

> **Install libraries mentioned in `requirements.txt`**

```python
make install_libraries
``` 

> **To create the entire struture with main folder name as `ml-project`**
```python
make build
```

> **To clean cached folders**
```python
make clean
```

## Approach 2

### Prerequisites
  The only prerequisites is to have python 3.x installed

> If you want a simpler route, just use the below command for creating the folder of your choice
folder_name is a required parameter and can be given any name as long as that folder does not exists.

```python
python template.py ml-project
```

# Project Structure

> The project structure looks complicated, but is quite simple actually
<img width="100%" src="https://github.com/rvbug/cookie-ml/blob/main/tree-structure.png" />

```
src - Most of your code lives in this folder e.g. main.py, preprocess.py, visualizer.py etc  
requirements.txt - If you use `conda` or `virtualenv` to  install ML libraries then update this file but if you 
prefer `pipenv` then replace it with Pipfile. Will be supporting this in the next release.

reports - All reports are stored here after data processing/cleaning.   
You might want send these to s3 bucket to be consumed by 3rd party visualization tools for further analysis. 
It can also store reports (xlsx, csv format) to be sent at regular intervals

plots - Storing graphs(png/jpg). This can be used for presentation/publishing papers/documentation

params.yaml - YAML file for storing configurations
 
notebook - Stores all your jupyter notebooks which is used during your experiment/research phase   
  nb_research - to store all your artifacts, notes, reference links.  
  nb_report - Storing all your sample reports   
  nb_model - For storing your params, model during your experiment phase  
  nb_data - Folder contains all the data used during your experiments.
  project_name_EDA_ML_Experiments.ipynb - filename is same as `project name`
  project_name.ipynb - Final clean code lives here. 
  
  data - folder contains all the data used during your experiments.

models - to store all the models you would have trained with lots of hyper params   

logs - stores the application log, this can be used consumed by tools e.g Promethus/Grafana  

docs - for building documentation - all your artifacts can be used for creating beautiful documentation
       You can use MKDocs / Docusaurus or similar static website generator for project documentation

data - to store data   
    train - For training you model  
    testing - For storing unseen data   
    raw - original data  
    processed - cleaned/transformed data which will be split into train or test data  

Readme.md - Landing page of your project which is a markdown file 
Makefile - To automate your script and it's dependencies if you are going to use it
```

# Future support
- create virtual env
- Support for DVC 
- Docker
- MKDocs & Docusaurus
- Adding files under src
   - main.py
   - __init__.py
   - preprocessing.py
