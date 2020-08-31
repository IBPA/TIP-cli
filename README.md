# TIP: Toxicology Integrated Platform

TIP (Toxicological Integrated Platform) provides a digital resource that (a) stores and integrates data from the labs that are part of the SRP center in UCD and (b) enables access to that data for both internal and external partners through an application programming interface (API).

## 1. Getting Started

This project is actively under the development. For more recent information, please check out the development branch https://github.com/IBPA/TIP/tree/dev.

### 1a. Installation
```
$ git clone https://github.com/IBPA/TIP.git  # Clone the repository to your machine.
$ pip install ./TIP  # Initiate setup.py.
```
Check if the package is correctly installed by
```
$ tip-cli
```

### 1b. How to Use

#### Data template generation

This is called when a user want to download a data template in order to upload their data. CLI sends a request to back end to retrieve the most recent data template. The default file name is 'output.csv' which stored at the current path.

Example:
```console
$ tip-cli gen-tmp  # Default output file, 'output.csv'
$ tip-cli gen-tmp -outfile ../template.csv  # Custom output file
```

#### Data creation

This is called when a user uploads their data to the database on the back end. It requires the path to the uploading data file. It will return response code and error to the user.

Example:
```console
$ tip-cli create -infile path/to/your/uploading/file.csv
$ tip-cli create -infile tip/client/cli/tests/data_dummy.csv  # example
```

#### Data read

This allows users to read the data on the database given a keyword. This action will not change any information on the database. Currently it is case-sensitive (e.g., 'a' VS. 'A'). It will print the search result to the console and print error if it fails. Use a query to specify the search filter. The query must follow these requirements:
- Each parameter is a pair of a field and a value.
- A field and a value are separated by exactly a colon.
- The first parameter must be 'type:compound' or 'type:assay', indicating the data type you are updating.
- Each parameter is separated by exactly a comma.
- Use quotes for strings containing whitespace(s), (e.g., comments.)
- Use semicolons for strings containing multiple values, (e.g., pmid.)

Example:
```console
$ tip-cli read -query type:compound,cid:962
```

#### Data update

This allows users to update specific fields of the data in the database. A user needs to provide a TID (TIP ID) of the data and a query which contains the information of updating fields and their new values.

Example:
```console
$ tip-cli update -tid 1 -query type:compound,comment:"You can spill it.",common_names:"Ice;Dihydrogen oxide"  # Updating 'comment' field of 'Water' compound.
```

#### Data delete

Users can also delete data that are already created by specifying the TID of the data. Users also need to specify either compound or assay data during the deletion. In the future, data deletion will be cooperated with user authentication so that only data can only be deleted by users who created them.

Example:
```console
$ tip-cli update -tid 1 -query type:compound # Deleting compound data with TID of 1.
```

### 1c. Uninstallation

```console
$ pip uninstall ./TIP
```

## 2. Authors

- **Fang Li** @ https://github.com/fangzhouli
- **Jason Youn** @ https://github.com/jasonyoun

## 3. Contact

For any questions, please contact us at tagkopouloslab@ucdavis.edu.

## 4. License

This project is licensed under the GNU GPLv3 License. Please see the <code>[LICENSE](./LICENSE)</code> file for details.

## 5. Acknowledgments

This work has been supported by UCD Superfund Research Center funded by NIH/NIEHS.
