# will always be called first
.DEFAULT_GOAL=help
FOLDER_NAME := ml-project

.ONESHELL:
install_libraries: # install libraries
	pip install -r requirements.txt

build:  # create ML folder structure
	python template.py $(FOLDER_NAME)

clean: # delete cache folders
	@rm -rf __pycache__

help: # arguments you can use
	@egrep -h '\s#\s' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?# "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'
