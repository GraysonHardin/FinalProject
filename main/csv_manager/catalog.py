from main.csv_manager.load_data import get_csv_data
from main.builders.vehicle_builder import VehicleBuilder

# Searches by the appropriate values
def search(search_by_make, search_by_model, search_by_year):
    _handle_invalid_search_terms(search_by_make, search_by_model, search_by_year)

    filtered_rows = _filter_rows(search_by_make, search_by_model, search_by_year)

    return _build_vehicles(filtered_rows)


def _filter_rows(make, model, year):
    csv_data = get_csv_data()

    def exists_in_row(row):
        return make in row and model in row and year in row

    return list(filter(exists_in_row, csv_data))


# This is built for input validation
def _handle_invalid_search_terms(search_by_make, search_by_model, search_by_year):
    if not search_by_make or not search_by_model or not search_by_year:
        raise ValueError('Please provide make, model, and year.')


def _build_vehicles(filtered_rows):
    vehicles = []
    for row in filtered_rows:
        vehicle = VehicleBuilder().values(
            make=row[0],
            model=row[1],
            year=row[2],
            mileage=row[3],
            price=row[4],
            color=row[5]
        )

        vehicles.append(vehicle)
    return vehicles
