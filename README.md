# TIP: Toxicology Integrated Platform

TIP (Toxicological Integrated Platform) provides a digital resource that
- stores and integrates data from the labs that are part of the SRP center in UCD,
- enables access to data for both internal and external partners through an application programming interface (API).

## 0. TODO

1. Encryption / HTTPS Phase 2
2. Handler - Logging rules

## Directories

* <code>[tip](./tip)</code>: The source code.
* <code>[examples](./examples)</code>: The tutorial with examples.

## Getting Started

This project is under an active development. For more recent updates, please check out the development branch https://github.com/IBPA/TIP/tree/dev.

### Installation
```
$ git clone https://github.com/IBPA/TIP.git  # Clone the repository to your machine.
$ pip install ./TIP  # Initiate setup.py.
```
Check if the package is correctly installed by
```
$ tip-cli
```

### Uninstallation

```console
$ pip uninstall tip-cli
```

## Authors

- **Fang Li** @ https://github.com/fangzhouli
- **Jason Youn** @ https://github.com/jasonyoun

## Contact

For any questions, please contact us at tagkopouloslab@ucdavis.edu.

## License

This project is licensed under the GNU GPLv3 License. Please see the <code>[LICENSE](./LICENSE)</code> file for details.

## Acknowledgments

This work has been supported by UCD Superfund Research Center funded by NIH/NIEHS.
