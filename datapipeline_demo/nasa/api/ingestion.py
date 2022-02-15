import datetime
from typing import Dict, List
from datapipeline_demo.nasa.api.types import WGS84Point
from datapipeline_demo.nasa.api.parsing import parse_era5_land

import requests

"""
Retrieve era5 data using the NASA rest api
https://power.larc.nasa.gov/docs/services/api/temporal/monthly/
"""

def datetime_to_str(date: datetime.date) -> str:
    return date.strftime("%Y%m%d")

def retrieve_nasa(
    start_date: datetime.date,
    end_date: datetime.date,
    location: WGS84Point,
    parameters:str,
) -> Dict[str, object]:

    # TODO(Smrithi) try to restructure the request_url/endpoint with yarl with example below
    # base_url = yarl.URL('https://power.larc.nasa.gov/')

    # print(base_url.with_path('api/temporal/daily/point').with_query('location=1234'))
    # query_dict ={
    #     'lat': location.latitude,
    #     'lon': location.longitude,
    #     ''
    # }


    # example: /api/temporal/daily/point?parameters=T2M&community=SB&longitude=0&latitude=0&start=20170101&end=20170201&format=JSON
    request_url = f"https://power.larc.nasa.gov/api/temporal/daily/point?parameters={parameters}&community=SB&longitude={location.longitude}&latitude={location.latitude}&start={datetime_to_str(start_date)}&end={datetime_to_str(end_date)}&format=JSON"
    resp = requests.get(request_url)
    resp.raise_for_status()

    # what you want after finishing the parsing function you want: return parse_era5_land(resp.json())
    return resp.json()

