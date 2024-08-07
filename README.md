# J-RSYNC

J-Rsync is a python wrapper on unix rsync which uses a json configuration file to identify what to sync.
The tool was designed to solve the problem of recurrently synchronising many directories or files

Using a single command from crontab, it is possible to keep synchronized many paths.

![Python](https://img.shields.io/badge/Python->3.10-blue.svg)
[![Anaconda](https://img.shields.io/badge/conda->22.11.1-green.svg)](https://anaconda.org/)
[![Pip](https://img.shields.io/badge/pip->19.0.3-brown.svg)](https://pypi.org/project/pip/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Pydantic v2](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/pydantic/pydantic/main/docs/badge/v2.json)](https://docs.pydantic.dev/latest/contributing/#badges)
[![Poetry](https://img.shields.io/endpoint?url=https://python-poetry.org/badge/v0.json)](https://python-poetry.org/)

---

## Installation

### Via PIP

```shell
pip install jrsync
```

### Via MAMBA/CONDA

```shell
mamba install jrsync
```

---

## Usage

```shell
usage: jrsync [-h] [--src-address SRC_ADDRESS] [--dst-address DST_ADDRESS]
              [--force] [-o OPTIONS] [-d--dry-run] [-V]
              config date_to_sync

Jrsync CLI

positional arguments:
  config                Json file containing sync information
  date_to_sync          Date in the format YYYYMMDD

options:
  -h, --help            show this help message and exit
  --src-address SRC_ADDRESS
                        Source address. Example: user@remote
  --dst-address DST_ADDRESS
                        Dest address. Example: user@remote
  --force               Allow to run multiple instance in the same moment
  -o OPTIONS, --options OPTIONS
                        Rsync options. use -o|--options= to avoid conflicts
                        with python args
  -d--dry-run           Enable dry run mode
  -V, --version         Print version and exit

```

### Remote synchronization

As default, the tool assumes that the path are local, but both source and destination path can be located on a remote
server.
**Be carefully that only one path can be remote**

#### Sync from remote to local

To synchronize files from remote to local computer:

```shell
jrsync <config> <date> --src-address user@remote
```

#### Sync from local to remote

To synchronize files from local to remote:

```shell
jrsync <config> <date> --dst-address user@remote
```

### Rsync options

As default, rsync runs with the following options:

```shell
-aP
```

They can be changed using `-o|--options`:

```shell
jrsync <config> <date> --options="-avug"
```

---

## Authors

- Antonio Mariani (antonio.mariani@cmcc.it)

---

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

---

## Contact

For any questions or suggestions, please open an issue on the project's GitHub repository.
