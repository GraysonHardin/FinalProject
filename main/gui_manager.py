import tkinter
import tkinter as tk

from main.database.create_rows import create_vehicle
from main.csv_manager.catalog import search
from main.csv_manager.vehicle_builder import VehicleBuilder
from tkinter import messagebox
from tkinter import *

from main.database.connect_to_db import create_connection
from main.database.create_tables import create_tables
from main.database.query_database import select_all_vehicles

m = tkinter.Tk()
m.geometry('1920x1080')
m.title('Catalog')


def handle_database_creation():
    create_connection("vehicle.db")
    create_tables("vehicle.db")
    # remove this line of code
    # with conn:
    #     vehicle = ('Ford', 'Mustang', '2016')
    #     create_vehicle(conn, vehicle)
    #     print(select_all_vehicles(conn))


catalog_searcher = VehicleBuilder

display_make_input_message = Label(text='Enter vehicle make')
display_model_input_message = Label(text='Enter vehicle model')
display_year_input_message = Label(text='Enter vehicle year')

display_make_input_message.grid(row=1, column=1)
display_model_input_message.grid(row=2, column=1)
display_year_input_message.grid(row=3, column=1)

add_vehicle_make_display_message = Label(text='Enter vehicle make')
add_vehicle_model_display_message = Label(text='Enter vehicle model')
add_vehicle_year_display_message = Label(text='Enter vehicle year')
add_vehicle_mileage_display_message = Label(text='Enter vehicle mileage')
add_vehicle_price_display_message = Label(text='Enter vehicle price')
add_vehicle_color_display_message = Label(text='Enter vehicle color')

add_vehicle_make_display_message.grid(row=5, column=1)
add_vehicle_model_display_message.grid(row=6, column=1)
add_vehicle_year_display_message.grid(row=7, column=1)
add_vehicle_mileage_display_message.grid(row=8, column=1)
add_vehicle_price_display_message.grid(row=9, column=1)
add_vehicle_color_display_message.grid(row=10, column=1)

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


def search_catalog():
    if make_input.get() and model_input.get() and year_input.get():
        search_results = search(make_input.get(), model_input.get(), year_input.get())
        print(search_results)
        draw_table(search_results)
    else:
        messagebox.showerror("Error, please provide make, model, and year ")
    model_input.delete(0, tk.END)
    make_input.delete(0, tk.END)
    year_input.delete(0, tk.END)


def add_vehicle():
    conn = create_connection("vehicle.db")

    with conn:
        vehicle = (add_vehicle_color_input.get(), add_vehicle_model_input.get(), add_vehicle_year_input.get(),
                   add_vehicle_mileage_input.get(), add_vehicle_price_input.get(), add_vehicle_color_input.get())

        # paid_for_price: 20000
        # sold_for: 30000

        try:
            create_vehicle(conn, vehicle)

        except:
            raise Exception('Vehicle database error')

        add_vehicle_make_input.delete(0, tk.END)
        add_vehicle_model_input.delete(0, tk.END)
        add_vehicle_year_input.delete(0, tk.END)
        add_vehicle_mileage_input.delete(0, tk.END)
        add_vehicle_price_input.delete(0, tk.END)
        add_vehicle_color_input.delete(0, tk.END)

        print(select_all_vehicles(conn))


def draw_table(rows):
    for i in range(len(rows)):
        column = 3
        for key in rows[i]:
            e = tkinter.Entry(m, width=20, fg='black', font=('Arial', 12, 'bold'))

            e.grid(row=i, column=column)
            e.insert(tkinter.END, rows[i][key])
            column += 1
            e['state'] = tkinter.DISABLED


create_search_button = tkinter.Button(m, text='Search Catalog', width=25, command=search_catalog)
create_search_button.grid(row=0, column=2)

create_add_vehicle_button = tkinter.Button(m, text='Add Vehicle to Database', width=25, command=add_vehicle)
create_add_vehicle_button.grid(row=4, column=2)

exit_button = tkinter.Button(m, text='Exit', width=25, command=m.destroy)
exit_button.grid(row=30, column=2)

handle_database_creation()
m.mainloop()
