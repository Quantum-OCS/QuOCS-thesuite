## QuOCS - The Suite

quocs-suite is the main executable script of the optimization library. It is based on the following repositories:
* the tools: https://github.com/Quantum-OCS/QuOCS-tools
* the optimization library: https://github.com/Quantum-OCS/QuOCS
* the PySide2 interface: https://github.com/Quantum-OCS/QuOCS-pyside2interface

## Unittesting

[![Build Status](https://github.com/Quantum-OCS/QuOCS-thesuite/actions/workflows/unit_testing_linux.yml/badge.svg)](https://github.com/Quantum-OCS/QuOCS-thesuite/actions)
[![Build Status](https://github.com/Quantum-OCS/QuOCS-thesuite/actions/workflows/unit_testing_windows.yml/badge.svg)](https://github.com/Quantum-OCS/QuOCS-thesuite/actions)

### Installation

Create a virtual environment
```bash
python3 -m venv quocs-venv
```
Activate the virtual environment
```bash
source quocs-venv/bin/activate
```
Install basic packages
```bash
python -m pip install --upgrade pip setuptools wheel
```
Install the quocs packages:
```bash
python -m pip install -e git+https://github.com/Quantum-OCS/QuOCS-thesuite#egg=quocs-thesuite
```
Now you can launch the programme with
```bash
quocs
```

### Examples
In the examples' folder you can find few config json files to be loaded in the gui
and used to test the PureParametrization and the dCRAB algorithm.
