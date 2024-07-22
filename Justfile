# list all available commands
default:
  just --list

###############################################################################
# Basic project and env management

# clean all generated build, python, and lint files
clean:
    rm -fr dist
    rm -fr .eggs
    find . -name '*.egg-info' -exec rm -fr {} +
    find . -name '*.egg' -exec rm -f {} +
    find . -name '*.pyc' -exec rm -f {} +
    find . -name '*.pyo' -exec rm -f {} +
    find . -name '*~' -exec rm -f {} +
    find . -name '__pycache__' -exec rm -fr {} +
    rm -fr .mypy_cache

# install with all deps
install:
	pip install uv
	uv pip install -r requirements.txt

# lint, format, and check all files
lint:
	pre-commit run --all-files

# unpack dataset archive
unpack-archive file:
  mkdir -p data
  tar -xvzf {{ file }}