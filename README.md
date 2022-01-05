# Introduction

If you want to start a new DS or ML project or ready to move to productionise the code, then you can use this cookie-ml to create your own custom folders
Run the following command

**`$ make help`**  - shows the lists of commands you can execute



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
If your target name is matching a file/folder then it will have conflicts. So to avoid that use `.PHONY`

## Variables
```
PIP_INSTALLATION := "pip install -r"
install:
	@echo {PIP_INSTALLATION}
```





