## QuOCS - The Suite
quocs-suite is the main executable script of the optimization library. It is based on the following repositories:
* the tools: https://github.com/Quantum-OCS/QuOCS-tools
* the optimization library: https://github.com/Quantum-OCS/QuOCS
* the PySide2 interface: https://github.com/Quantum-OCS/QuOCS-pyside2interface

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
python -m pip install -e git+https://github.com/Quantum-OCS/QuOCS#egg=quocs_lib 
python -m pip install -e git+https://github.com/Quantum-OCS/QuOCS-pyside2interface#egg=quocs_pyside2interface
```
Now you can launch the suite in the main folder
```bash
python quocs-thesuite.py
```

### Examples
In the examples' folder you can find few config json files to be loaded in the gui
and used to test the PureParametrization and the dCRAb algorithm.
