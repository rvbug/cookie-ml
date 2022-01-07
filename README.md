# Preface

I am working on introduction to **make** and **Makefile**, which I share it shortly :-

Do visit my article[] and leave a feedback.

# Introduction


You have trained your model using `jupyter notebook` / `vscode` / `pycharm`.   
Getting your code into production is a whole new challenge unlike any other you have done before.  

It is chaotic but has a stucture to it. 

# About this project

Helps you to build a project struture easily and is quite flexible.  
Developed in Python 3, you can use it via make or calling python script


# Approches

There are couple of ways you can use this project.

1. make & Makefile  

2. run script directly.


## Approach 1

*`make`* is a utility and a very popluar for automating your compilation of C/C++ programs and their dependencies.


`make` runs the scripts mentioned in `Makefile`

Once you clone this repo, call `make` from command line, by default it will show all the arguments you can use
<img src="">

The order of execution is as follows :

To see the arguments
```python
make help
```

Install libraries mentioned in 'requirements.txt'

```python
`make install_libraries` 
``` 

To create the entire struture with main folder name as *ml-project*
```python
`make build` 
```

To clean cached folders
```python
`make clean`
```

## Approach 2

If you want a simpler route, just use the below command for creating the folder of your choice
folder_name is a required parameter and can be given any name as long as that folder does not exists.

```python
python template.py ml-project
```


# Project Structure

The project structure looks complicated, but is quite simple
<img width="100%" src="https://github.com/rvbug/cookie-ml/blob/main/tree-structure.png" />



# future support
- Modify Makefile for virtual env
- MKDocs & Docusaurus

