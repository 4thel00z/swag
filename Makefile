install: ## Install the dependencies
	poetry install

update: ## Update the dependencies
	poetry update

shell: ## Enter the virtualenv
	poetry shell

run: ## Run the swag cli
	poetry run python3 swag/__main__.py
help: FORCE          ## Show this help.
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep  | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'  

FORCE:
