import dataclasses as dc
from typing import List

@dc.dataclass
class DailyWeather:
    lat: float
    lon: float
    temperature_avg: float
    temperature_min: float
    temperature_max: float


def parse_era5_land(response: dict) -> List[DailyWeather]:
    # TODO (Smrithi)
    """
    example response
    {'type': 'Feature', 'geometry': {'type': 'Point', 'coordinates': [20.09, -23.023, 1277.67]}, 'properties': {'parameter': {'T2M': {'20170101': 25.56, '20170102': 25.48, '20170103': 26.03, '20170104': 25.28, '20170105': 22.85, '20170106': 23.83, '20170107': 25.6, '20170108': 25.99, '20170109': 23.1, '20170110': 24.61, '20170111': 24.51, '20170112': 22.79, '20170113': 22.23, '20170114': 24.92, '20170115': 26.55, '20170116': 27.05, '20170117': 26.03, '20170118': 23.35, '20170119': 25.18, '20170120': 27.04, '20170121': 27.61, '20170122': 25.93, '20170123': 25.3, '20170124': 23.62, '20170125': 24.75, '20170126': 25.61, '20170127': 25.76, '20170128': 25.23, '20170129': 25.97, '20170130': 26.62, '20170131': 26.41}}}, 'header': {'title': 'NASA/POWER CERES/MERRA2 Native Resolution Daily Data', 'api': {'version': 'v2.2.18', 'name': 'POWER Daily API'}, 'fill_value': -999.0, 'start': '20170101', 'end': '20170131'}, 'messages': [], 'parameters': {'T2M': {'units': 'C', 'longname': 'Temperature at 2 Meters'}}, 'times': {'data': 2.246, 'process': 0.02}}
    """
    res = []
    temps = response['properties']['parameter']['T2M']   
    location = response['geometry']['coordinates']
    
    # TODO (Smrithi )
    for k, v in temps.items():
      res += DailyWeather(
          lat=
          lon=
          temperature_avg=

      )  
    
    pass

# with example reponse
resp = {'type': 'Feature', 'geometry': {'type': 'Point', 'coordinates': [20.09, -23.023, 1277.67]}, 'properties': {'parameter': {'T2M': {'20170101': 25.56, '20170102': 25.48, '20170103': 26.03, '20170104': 25.28, '20170105': 22.85, '20170106': 23.83, '20170107': 25.6, '20170108': 25.99, '20170109': 23.1, '20170110': 24.61, '20170111': 24.51, '20170112': 22.79, '20170113': 22.23, '20170114': 24.92, '20170115': 26.55, '20170116': 27.05, '20170117': 26.03, '20170118': 23.35, '20170119': 25.18, '20170120': 27.04, '20170121': 27.61, '20170122': 25.93, '20170123': 25.3, '20170124': 23.62, '20170125': 24.75, '20170126': 25.61, '20170127': 25.76, '20170128': 25.23, '20170129': 25.97, '20170130': 26.62, '20170131': 26.41}}}, 'header': {'title': 'NASA/POWER CERES/MERRA2 Native Resolution Daily Data', 'api': {'version': 'v2.2.18', 'name': 'POWER Daily API'}, 'fill_value': -999.0, 'start': '20170101', 'end': '20170131'}, 'messages': [], 'parameters': {'T2M': {'units': 'C', 'longname': 'Temperature at 2 Meters'}}, 'times': {'data': 2.246, 'process': 0.02}}
parse_era5_land(resp)