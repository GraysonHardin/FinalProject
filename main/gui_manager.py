import tkinter
import tkinter as tk

from main.builders.purchased_vehicle_builder import PurchasedVehicleBuilder
from main.database.create_rows import create_vehicle, update_vehicle
from main.csv_manager.catalog import search
from main.csv_manager.vehicle_builder import VehicleBuilder
from tkinter import messagebox

from main.database.connect_to_db import create_connection
from main.database.create_tables import create_tables
from main.database.query_database import select_all_vehicles
from main.csv_manager.monthly_sales_report import monthly_sales_report
from main.labels import draw_labels
from main.view_catalog_table import open_catalog_table
from main.view_inventory_table import open_inventory_table

m = tkinter.Tk()
m.geometry('1920x1080')
m.title('Catalog')
draw_labels(m)


def handle_database_creation():
    create_connection("vehicle.db")
    create_tables("vehicle.db")


catalog_searcher = VehicleBuilder

# Lines 42-49 are for search_catalog values
make_input = tk.Entry(m, width=25)
make_input.grid(row=1, column=2)

model_input = tk.Entry(m, width=25)
model_input.grid(row=2, column=2)

year_input = tk.Entry(m, width=25)
year_input.grid(row=3, column=2)

# Lines 52-66 are for add_vehicle values
add_vehicle_make_input = tk.Entry(m, width=25)
add_vehicle_make_input.grid(row=5, column=2)

add_vehicle_model_input = tk.Entry(m, width=25)
add_vehicle_model_input.grid(row=6, column=2)

add_vehicle_year_input = tk.Entry(m, width=25)
add_vehicle_year_input.grid(row=7, column=2)

add_vehicle_mileage_input = tk.Entry(m, width=25)
add_vehicle_mileage_input.grid(row=8, column=2)

add_vehicle_price_input = tk.Entry(m, width=25)
add_vehicle_price_input.grid(row=9, column=2)

add_vehicle_color_input = tk.Entry(m, width=25)
add_vehicle_color_input.grid(row=10, column=2)

add_vehicle_paid_for_price = tk.Entry(m, width=25)
add_vehicle_paid_for_price.grid(row=11, column=2)

add_vehicle_sold_for_price = tk.Entry(m, width=25)
add_vehicle_sold_for_price.grid(row=12, column=2)

add_vehicle_id = tk.Entry(m, width=25)
add_vehicle_id.grid(row=13, column=2)




def search_catalog():
    if make_input.get() and model_input.get() and year_input.get():
        search_results = search(make_input.get(), model_input.get(), year_input.get())

        open_catalog_table(m, search_results)
    else:
        messagebox.showerror("Error, please provide make, model, and year ")
    model_input.delete(0, tk.END)
    make_input.delete(0, tk.END)
    year_input.delete(0, tk.END)


def add_vehicle():
    conn = create_connection("vehicle.db")

    with conn:
        vehicle = (
            add_vehicle_make_input.get(),
            add_vehicle_model_input.get(),
            add_vehicle_year_input.get(),
            add_vehicle_mileage_input.get(),
            add_vehicle_price_input.get(),
            add_vehicle_color_input.get(),
            add_vehicle_paid_for_price.get(),
            add_vehicle_sold_for_price.get()
        )

        try:
            if add_vehicle_id.get():
                update_vehicle_tuple = (add_vehicle_sold_for_price.get(), add_vehicle_id.get())
                update_vehicle(conn, update_vehicle_tuple)
            else:
                create_vehicle(conn, vehicle)

        except:
            raise Exception('Vehicle database error')

        add_vehicle_make_input.delete(0, tk.END)
        add_vehicle_model_input.delete(0, tk.END)
        add_vehicle_year_input.delete(0, tk.END)
        add_vehicle_mileage_input.delete(0, tk.END)
        add_vehicle_price_input.delete(0, tk.END)
        add_vehicle_color_input.delete(0, tk.END)
        add_vehicle_paid_for_price.delete(0, tk.END)
        add_vehicle_sold_for_price.delete(0, tk.END)
        add_vehicle_id.delete(0, tk.END)


def _build_vehicles(rows):
    vehicles = []
    for row in rows:
        vehicle = PurchasedVehicleBuilder(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])

        vehicles.append(vehicle.values())
    return vehicles


def view_inventory():
    conn = create_connection("vehicle.db")

    with conn:
        rows = select_all_vehicles(conn)

        open_inventory_table(m, _build_vehicles(rows))


def write_to_csv():
    conn = create_connection("vehicle.db")

    with conn:
        rows = select_all_vehicles(conn)

        monthly_sales_report(_build_vehicles(rows))


create_search_button = tkinter.Button(m, text='Search Catalog', width=25, command=search_catalog)
create_search_button.grid(row=0, column=2)

create_add_vehicle_button = tkinter.Button(m, text='Add/Update Vehicle to Database', width=25, command=add_vehicle)
create_add_vehicle_button.grid(row=4, column=2)
open_window = tkinter.Button(m, text='View Vehicle Inventory', width=25, command=view_inventory)
open_window.grid(row=31, column=2)

monthly_sales_report_button = tkinter.Button(m, text='View Monthly Sales Report', width=25, command=write_to_csv)
monthly_sales_report_button.grid(row=29, column=2)

exit_button = tkinter.Button(m, text='Exit', width=25, command=m.destroy)
exit_button.grid(row=30, column=2)

handle_database_creation()
m.mainloop()
