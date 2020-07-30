# TIP-CLI: TIP Command-line Interface

## Introduction

The goal of TIP-CLI module is to provide the basic command-line interface (CLI) for both developers and future users. Currently, CLI is under the testing, and this tutorial is mainly focusing on internal use.

## Installation

1. Install NodeJS: https://nodejs.org/en/.
2. Install TIP command-line interface (CLI):
```
$ git clone git@github.com:IBPA/TIP.git  # Clone the repository to your machine.
$ cd path/to/TIP  # This will be the root directory.
$ pip install ./tip/client/cli  # Initiate setup.py.
```

## Usage

1. Open the terminal and send requests to the back end from CLI:
```
$ tip-cli -h
usage: tip-cli [-h] [-user [USER]] [-pw [PW]] [-infile [INFILE]] [-outfile [OUTFILE]] {gen-tmp,create,read,update,delete}
```

## Test

For internal quality assurance.

### Data template generation

This is called when a user want to download a data template in order to upload their data. CLI sends a request to back end to retrieve the most recent data template. The default file name is 'output.csv' which stored at the current path.
```console
$ tip-cli gen-tmp  # Default output file, 'output.csv'
$ tip-cli gen-tmp -outfile ../template.csv  # Custom output file
```

### Data creation

This is called when a user uploads their data to the database on the back end. It requires the user to provide user name, password, and the path to the uploading data file. This will norify the back end to print your uploaded data on its console.
```console
$ tip-cli create -user fzli -pw abc -infile path/to/uploading/data.csv
$ tip-cli create -user fzli -pw abc -infile tip/client/cli/tests/data_dummy.csv  # example
```
This should create new data on the Mongo database.

### Data read

This allows user to read the data on the database given a keyword. This action will not change any information on the database. Currently it is case-sensitive, and it only searches keywords in compound names.
```console
$ tip-cli read -keywords Water
```
This should return a compound information along with its assay data.

### Uninstallation

Before remove the directory of TIP, run the following command:

```console
pip uninstall tip-cli
```

## Authors

- Fang Li - https://github.com/fangzhouli
- Jason Youn - https://github.com/jasonyoun

## Acknowledgments

This work has been supported by UCD Superfund Research Center funded by NIH/NIEHS.

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
