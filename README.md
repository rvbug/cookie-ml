
# Introduction

All ML projects start with basic understanding of data and experiement with Jupyter notebook (mostly) and then gradually moving to a proper IDE, writing/reusing helper functions, seperating data_pipline code with data processing etc. It is chaotic for beginners but that is the beauty of it.


# About this project

I use a specific ML project structure. It helps me focus on getting started immediately on any project. It contains a simple python script and a configurable folder structure in YAML format.
This is extemely simple to use command line script.


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
- create virtual env (In progress)
- Add new folders - conf/ and validate under data
- Add .gitignore file
- Support for DVC, MLFlow & Tensorboard
- Docker
- MKDocs & Docusaurus
- Installation mode
- Adding files under src
   - main.py
   - __init__.py
   - preprocessing.py
