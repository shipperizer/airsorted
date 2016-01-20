.PHONY: test run install help

PIP?=pip3
PYTEST?=py.test
PYTHON?=python3

install:
	$(PIP) install -r requirements.txt

test:
	$(PYTEST) test/

run:
	$(PYTHON) airsorted.py

help:
	@printf "to launch the program use 'make run' or 'python airsorted.py' \n"
	@printf "to install dependencies run 'make install' or use pip with the requirements file \n"
	@printf "to launch the tests just run 'make test' or 'py.test test' \n"
