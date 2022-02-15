from datapipeline_demo.nasa.api.ingestion import retrieve_nasa_daily


def main():
    body = retrieve_nasa_daily(
        start_date="20170101",
        end_date="20170201",
        lat=-26.204734,
        lon=-54.382324,
        parameters="T2M",
    )
    print(body)


if __name__ == "__main__":
    main()
