from csv import reader


def get_csv_data():
    open_csv_file = open("vehicle_catalog.csv")

    return reader(open_csv_file, delimiter=',')
