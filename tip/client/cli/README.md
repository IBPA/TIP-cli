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

This is called when a user uploads their data to the database on the back end. It requires the path to the uploading data file. It will return response code and error to the user.
```console
$ tip-cli create -infile path/to/uploading/data.csv
$ tip-cli create -infile tip/client/cli/tests/data_dummy.csv  # example
```

### Data read

This allows users to read the data on the database given a keyword. This action will not change any information on the database. Currently it is case-sensitive (e.g., 'a' VS. 'A'), and it only searches keywords in compound names. It will print the search result to the console and print error if it fails.
```console
$ tip-cli read -keywords Water
```

### Data update

This allows users to update specific fields of the data in the database. A user needs to provide a TID (TIP ID) of the data and a query which contains the information of updating fields and their new values. The query must follow these requirements:
- Each parameter is a pair of a field and a value.
- A field and a value are separated by exactly a colon.
- The first parameter must be 'type:compound' or 'type:assay', indicating the data type you are updating.
- Each parameter is separated by exactly a comma.
- Use quotes for strings containing whitespace(s), (e.g., comments.)
- Use semicolons for strings containing multiple values, (e.g., pmid.)
```console
$ tip-cli update -tid 5f360c170d5b10949c15b40e -query type:compound,comment:"You can spill it.",common_names:"Ice;Dihydrogen oxide"  # example of updating 'comment' field of 'Water' compound.
```

## Uninstallation

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
