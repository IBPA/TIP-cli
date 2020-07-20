# TIP: Toxicology Integrated Platform

## Introduction

The goal of TIP is to build a digital resource that (a) stores and integrates data from the labs that are part of the SRP center in UCD and (b) enables access to that data for both internal and external partners through an application programming interface (API), a command line interface and later on a web interface.

## Installation

1. Install NodeJS: https://nodejs.org/en/.
2. Install TIP command-line interface (CLI):
```
pip install tip/app/client/cli
```

## Usage

1. Run the following on the terminal to start running the server on your local:
```
cd tip/app/server
npm install
node controllers.js
```
2. Open another terminal and send requests to the back end from CLI:
```
$ tip-cli
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
path/to/TIP/tip/app/client$ tip-cli crerate -user fzli -pw abc123! -infile tests/data_dummy.csv
2020-07-11 18:00:40,105 INFO handler.py: Requesting to create data...
2020-07-11 18:00:40,105 INFO converter.py: Converting uploaded CSV file into JSON data format...
2020-07-11 18:00:40,115 DEBUG connectionpool.py: Starting new HTTP connection (1): localhost:3000
2020-07-11 18:00:40,126 DEBUG connectionpool.py: http://localhost:3000 "POST /api/upload HTTP/1.1" 200 17
```

### Uninstallation

Before remove the directory of TIP, run the following command:

```console
pip uninstall tip-client-cli
```

## Authors

- Fang Li - https://github.com/fangzhouli
- Jason Youn - https://github.com/jasonyoun

## Acknowledgments

This work has been supported by UCD Superfund Research Center funded by NIH/NIEHS.

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
