# Lemanscope Quality Assurance

[![License: MIT][mit-by-shield]][mit-by] ![Python][python-by-shield]

Quality assurance for the Lemanscope crowdsourced data. The quality assured data is then made available on the Lemanscope 
website https://lemanscope.org/

## Installation
Clone the repository and install it manually:
```commandline
git clone git@github.com:eawag-surface-waters-research/lemanscope_qa.git
cd lemanscope_qa
pip install requirements.txt
```
It is suggested to install the python packages in a virtual environment

## Usage

### Command line

```commandline
python src/main.py
```

### Arguments

Run the help command for a list of arguments

```commandline
python src/main.py --help
```

## License
This package is licensed under the MIT License.

[mit-by]: https://opensource.org/licenses/MIT
[mit-by-shield]: https://img.shields.io/badge/License-MIT-g.svg
[python-by-shield]: https://img.shields.io/badge/Python-3.9-g
[simstrat]: https://github.com/Eawag-AppliedSystemAnalysis/Simstrat
[scipy]: https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.minimize.html
[pest]: https://pesthomepage.org/