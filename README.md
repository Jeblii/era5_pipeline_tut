"""
We will build a ETL pipeline:
- Extract: NASA Power API -> result: json response

TODO (Smrithi)
- Transform: 
  - Parse the json into something in Python e.g. dataclass
  - Apply transformations
- Load (store somewhere else): 
  - We want to monthly report of the data 
  - The reported in postgres
"""