# Dependency Graph - Units of Innovation -- Analysis

## Setup

### Installing Dependencies

```bash
pip install -r requirements.txt
```

(or with [just](https://github.com/casey/just): `just install`)

## Downloading Data

The easiest mechanism we have for sharing the data is via GDrive.

GDrive link: []()

### With Just

The data management can be handled for you with:
`just unpack-data <path-to-downloaded-file>`

For example:

`just unpack-data ~/Downloads/per-day-pkg-releases-metrics.tar.gz`

### Manually

Untar the downloaded file and place the data in the `data` directory.

```
data
└── per-day-pkg-releases-metrics
    ├── 2020-02-07.parquet
    ├── 2020-02-08.parquet
    ├── 2020-02-09.parquet
    ├── 2020-02-10.parquet
    ├── 2020-02-11.parquet
    ├── 2020-02-12.parquet
    ├── 2020-02-13.parquet
    ├── 2020-02-14.parquet
    ├── 2020-02-15.parquet
    ...
```

## Development

You can lint and format your notebooks via [just](https://github.com/casey/just):

```
Available recipes:
    clean               # clean all generated build, python, and lint files
    default             # list all available commands
    install             # install with all deps
    lint                # lint, format, and check all files
    unpack-archive file # unpack dataset archive
```
