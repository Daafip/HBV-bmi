import xarray as xr
from pathlib import Path
import json
import dask


def read_config(config_file: str) -> dict:
    with open(config_file) as cfg:
        config = json.load(cfg)
    return config


def load_var(ncfile: str | Path, varname: str) -> xr.DataArray:
    """Load the precipitation data file generated by GenericLumpedForcing.


    .. code-block:: python

        from ewatercycle.base.forcing import GenericLumpedForcing

        shape = Path("./src/ewatercycle/testing/data/Rhine/Rhine.shp")
        cmip_dataset = {
            "dataset": "EC-Earth3",
            "project": "CMIP6",
            "grid": "gr",
            "exp": ["historical",],
            "ensemble": "r6i1p1f1",
        }

        forcing = GenericLumpedForcing.generate(
            dataset=cmip_dataset,
            start_time="2000-01-01T00:00:00Z",
            end_time="2001-01-01T00:00:00Z",
            shape=shape.absolute(),
        )

        data = load_precip(forcing.directory / forcing.pr)
    """
    with dask.config.set(scheduler="synchronous"):
        data = xr.load_dataset(ncfile)
    assert "time" in data.dims
    assert varname in data.data_vars
    return data[varname]
