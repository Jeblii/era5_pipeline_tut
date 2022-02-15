import datetime
from typing import Dict, List

import requests

"""
Retrieve era5 data using the CDS API
"""

# https://cds.climate.copernicus.eu/cdsapp#!/dataset/reanalysis-era5-land?tab=overview
# https://confluence.ecmwf.int/display/CKB/Climate+Data+Store+%28CDS%29+API+Keywords


def retrieve_nasa_daily(
    start_date: str,
    end_date: str,
    lat: float,
    lon: float,
    parameters=str,
) -> Dict[str, object]:

    # example: /api/temporal/daily/point?parameters=T2M&community=SB&longitude=0&latitude=0&start=20170101&end=20170201&format=JSON
    request_url = f"https://power.larc.nasa.gov/api/temporal/daily/point?parameters={parameters}&community=SB&longitude={lon}&latitude={lat}&start={start_date}&end={end_date}&format=JSON"
    resp = requests.get(request_url)
    resp.raise_for_status()
    return resp.json()