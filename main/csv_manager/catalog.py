from main.csv_manager.load_data import get_csv_data
from main.csv_manager.vehicle_builder import VehicleBuilder
from tkinter import messagebox


def search(search_by_make, search_by_model, search_by_year):
    _handle_invalid_search_terms(search_by_make, search_by_model, search_by_year)

    filtered_rows = _filter_rows(search_by_make, search_by_model, search_by_year)

    return _build_vehicles(filtered_rows)


def _filter_rows(make, model, year):
    csv_data = get_csv_data()

    def exists_in_row(row):
        return make in row and model in row and year in row

    return list(filter(exists_in_row, csv_data))


def _handle_invalid_search_terms(search_by_make, search_by_model, search_by_year):
    if not search_by_make or not search_by_model or not search_by_year:
       #raise ValueError('Please provide make, model, and year.')
        messagebox.showerror("Error", "Error message")




def _build_vehicles(filtered_rows):
    vehicles = []
    for row in filtered_rows:
        vehicle = VehicleBuilder(row[0], row[1], row[2], row[3], row[4], row[5])

        vehicles.append(vehicle.values())
    return vehicles
