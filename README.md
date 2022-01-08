# Preface

I am working on introduction to **make** and **Makefile**, which I share it shortly :-

Do visit my article[] and leave a feedback.

# Introduction


You have trained your model using `jupyter notebook` / `vscode` / `pycharm`.   
Getting your code into production is a whole new challenge unlike any other you have done before.  

It is chaotic but that is the beauty of it

# About this project

Helps you to build a project struture easily and is quite flexible.  
Developed in Python 3, you can use it via make or calling python script
Most importantly, it is extremely simple to use!

# Approches

There are couple of ways you can use this.

1. make & Makefile  

2. run script directly.


## Approach 1

*`make`* is a utility and a very popluar for automating the compilation of C/C++ programs and their dependencies.


`make` runs the scripts mentioned in `Makefile`

Once you clone this repo, call `make` from command line, by default it will show all the arguments you can use
<p>
<img src="https://github.com/rvbug/cookie-ml/blob/main/make.png">

The order of execution is as follows :

To see the arguments as above 
```python
make help
```

Install libraries mentioned in 'requirements.txt'

```python
make install_libraries
``` 

To create the entire struture with main folder name as *ml-project*
```python
make build
```

To clean cached folders
```python
make clean
```

## Approach 2

If you want a simpler route, just use the below command for creating the folder of your choice
folder_name is a required parameter and can be given any name as long as that folder does not exists.

```python
python template.py ml-project
```

# Project Structure

The project structure looks complicated, but is quite simple actually
<img width="100%" src="https://github.com/rvbug/cookie-ml/blob/main/tree-structure.png" />

```
Folder src - Most of your code lives here e.g. main.py, preprocess.py, visualizer.py etc  

Folder reports - Once you clean your data, you might want extract/send the processed data to s3 bucket.
          It can then been consumed by 3rd party tools for further analysis/visualization  

Folder plots - Graphs(png/jpg). This can be used for presentation/publising papers/documentation

params.yaml - YAML file for storing configuration
 
Folder notebook - All your jupyter notebooks which is used during your experiement/research phase   
 * Sub folder research - to store all your artifacts, notes, reference links. 
   * project_name_EDA_ML_Experiements.ipynb - filename is same as `project name`
 * Sub folder nb_report - Stores all your sample reports 
 
 * Sub folder nb_model - to store your params, model during your expermient phase
  
 * project_name.ipynb - Final clean code lives here. 
 * data - folder contains all the data used during your experiements.
 
models - to store all the models you would have trained with lots of hyper params  

logs - stores the application log, this can be used consumed by tools e.g Promethus/Grafana  

docs - for building documentation - all your artifacts can be used for creating beautiful documentation
       You can use MKDocs / Docusaurus or similar static website generator for project documentation

data - to store data   
  * train - For training you model  
  * testing - For storing unseen data   
  * raw - original data  
  * processed - cleaned/transformed data which will be split into train or test data  

Readme.md - Landing page of your project which is a markdown file 
Makefile - To automate your script and it's dependencies if you are going to use it

```

# future support
- create virtual env
- Support for DVC 
- MKDocs & Docusaurus

