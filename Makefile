.DEFAULT_GOAL=help

test: # testing
        @echo "test"

env: # env check
        @echo "env"

help: # select the target to run
        @egrep -h '\s#\s' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?# "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'
