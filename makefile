VENV=.venv
SHELL=/bin/bash
DJANGO_PROJECT=clinux

SYSPYTHON?=python3
python=$(VENV)/bin/python3
pip=$(python) -m pip
django=$(python) $(DJANGO_PROJECT)/manage.py

# Utility scripts to prettify echo outputs
bold := '\033[1m'
sgr0 := '\033[0m'

.PHONY: init
init: venv update

.PHONY: clean
clean:
	@echo -e $(bold)Clean up old virtualenv and cache$(sgr0)
	rm -rf $(VENV) *.egg-info

.PHONY: venv
venv: clean
	@echo -e $(bold)Create virtualenv$(sgr0)
	$(SYSPYTHON) -m venv $(VENV)
	$(pip) install --upgrade pip pip-tools

.PHONY: update
update:
	@echo -e $(bold)Install and update requirements$(sgr0)
	$(python) -m piptools sync

.PHONY: requirements
requirements: 
	@$(python) -m piptools compile -vU --all-extras \
		--resolver backtracking --output-file requirements.txt pyproject.toml

.PHONY: test
test:
	$(python) -m pytest -x -p no:warnings

.PHONY: lint
lint:
	$(python) -m black $(DJANGO_PROJECT)
	$(python) -m isort $(DJANGO_PROJECT)

.PHONY: secret-key
secret-key:
	$(python) -c 'from django.core.management.utils import get_random_secret_key; print(f"SECRET_KEY=\"{get_random_secret_key()}\"")' > .env

.PHONY: migrate migrations
migrate:
	$(django) migrate

migrations:
	$(django) makemigrations

.PHONY: serve runserver
serve: runserver
runserver:
	$(django) runserver
	