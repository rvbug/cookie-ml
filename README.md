# Introduction

If you want to start a new DS or ML project or ready to move to productionise the code, then you can use this cookie-ml to create your own custom folders
Run the following command

**`$ make help`**  - shows the lists of commands you can execute

If you already know about makefile or just want to create the folder directly
**`make install`**



But if you would like to know more about **make** and **Makefile** read on :-

## Makefile Introduction

make is a utility which helps to recompile code and it's dependencies automatically and uses Makefile. 

If you have worked on large scale C applications, you will be quite familar with the advantange of this utility.

Every Makefile has 3 things target, dependency & recipe. It looks something like this. Recepie is another word for command.
There is a tab before the recipe is provided.

```
target: dependency
	recipe
```
To run the make command use- **`make target`**


## Example
Below is a simple example, when you run 
**`make second`** - it will run the dependency first and then it's recepie. If you want to run only first target then call **`make first`**

```
first:
	@echo "run this first"

second: runfirst:
	@echo "running now"
```


Let us look at few things to get up and running quickly...

## PHONY
If your target name is matching a file/folder then it will have conflicts. So to avoid that use `.PHONY`. In below example a folder called "clean" will have conflict. Declare a target clean as .PHONY. Now this will ensure that the recipe is run regardless of file name 'clean' 


## Variables
```
PIP_INSTALLATION := "pip install -r"
install:
	@echo (PIP_INSTALLATION)
```

## Shell
Each recepie gets executed in a seperate shell but some time you need the same sheel where you declare the enviornment variables necessary for the project. 
To solve this use `.ONESHELL`




