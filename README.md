# Dependency Graph - Units of Innovation -- Analysis

## Setup

**Use Python 3.11 or 3.12.**

```bash
pip install -r requirements.txt
```

(or with [just](https://github.com/casey/just): `just install`)

## Downloading Data

After installing the required dependencies, you can download each dataset with: 
`python download.py <dataset-name>`

For example: `python download.py per-day-pkg-releases-metrics-one-year`

This will create an `archives` directory with the downloaded archive file
and a `data` directory with the extracted data.

All of the notebooks are configured to look for the correct
set of data files in the `data` directory by default so you should not need to
change any of the data reading configuration in the notebooks.

### Available Datasets

- `per-day-pkg-releases-metrics-one-year`
- `per-day-pkg-releases-metrics-two-year`
- `per-day-pkg-releases-metrics-six-months`
- `per-day-release-content-metrics-one-year-rated`

## Development

You can lint and format your notebooks via [just](https://github.com/casey/just):

```
Available recipes:
    clean   # clean all generated build, python, and lint files
    default # list all available commands
    install # install with all deps
    lint    # lint, format, and check all files
```
