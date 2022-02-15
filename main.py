from datetime import datetime
from email.mime import base
from datapipeline_demo.nasa.api.ingestion import retrieve_nasa
from datapipeline_demo.nasa.api.types import WGS84Point
import datetime
from datetime import timedelta
import yarl

def main():
    start_date = datetime.date(2017, 1, 1)
    end_date = start_date + timedelta(days=30)

    body = retrieve_nasa(
        start_date=start_date,
        end_date=end_date,
        location=WGS84Point(latitude=-23.023, longitude=20.09),
        parameters="T2M",
    )
    print(body)


if __name__ == "__main__":
    main()
