# HBV-BMI

[![PyPI](https://img.shields.io/pypi/v/HBV)](https://pypi.org/project/HBV/)

Basic Model Interface (BMI) HBV model intended for use with [eWaterCycle](https://github.com/eWaterCycle). See Repo said repo for instalation instructions. 

 HBV (Hydrologiska Byråns Vattenbalansavdelning) is a conceptual hydrological model. For more information on it's history, see this [paper](https://hess.copernicus.org/articles/26/1371/2022/).

This current implementation is _without_ a snow reservoir. 

Actual eWatercycle model wrapper can be found on [github](https://github.com/Daafip/ewatercycle-hbv)


## seperate use
Can also be used as a standalone package _in theory_ - not advised:

```console
pip install HBV
```

Then HBV becomes available as one of the eWaterCycle models

```python
from HBV import HBV

model = HBV()

....
```

Be aware of the non intuitive [BMI](https://github.com/eWaterCycle/grpc4bmi) implementation as this package is designed to run in a [docker](https://github.com/Daafip/HBV-bmi/pkgs/container/hbv-bmi-grpc4bmi) container. 


### Changelog

#### v1.0.0 
- working basic version after various [testing versions](https://test.pypi.org/project/HBV/)
#### v1.0.1 - v1.0.3 
- bug fixes etc (last time using live as a dev branch -> bad practive)
#### v1.1.0 
- added support for updating memory vector on the fly for Data assimilation. 

