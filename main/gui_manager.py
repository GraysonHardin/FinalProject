import tkinter
import tkinter as tk
from main.csv_manager.catalog import search, _handle_invalid_search_terms
from main.csv_manager.vehicle_builder import VehicleBuilder
from tkinter import messagebox
from tkinter import *

m = tkinter.Tk()
m.geometry('1920x1080')
m.title('Catalog')

# 1. Add error message in pop-up window when there is invalid search terms


catalog_searcher = VehicleBuilder

display_make_input_message = Label(text='Enter vehicle make ')
display_model_input_message = Label(text='Enter vehicle model')
display_year_input_message = Label(text='Enter vehicle year')

display_make_input_message.place(x=200, y=25)
display_model_input_message.place(x=200, y=45)
display_year_input_message.place(x=200, y=65)

make_input = tk.Entry(m, width=25)
make_input.grid(row=1)

model_input = tk.Entry(m, width=25)
model_input.grid(row=2)

year_input = tk.Entry(m, width=25)
year_input.grid(row=3)


def search_catalog():
    search_results = search(make_input.get(), model_input.get(), year_input.get())
    print(search_results)
    draw_table(search_results)
    model_input.delete(0, tk.END)
    make_input.delete(0, tk.END)
    year_input.delete(0, tk.END)


def draw_table(rows):
    for i in range(len(rows)):
        column = 1
        for key in rows[i]:
            e = tkinter.Entry(m, width=20, fg='black', font=('Arial', 12, 'bold'))

            e.grid(row=i, column=column)
            e.insert(tkinter.END, rows[i][key])
            column += 1
            e['state'] = tkinter.DISABLED


def handle_error_messages():
    raise_error = messagebox.showerror("Error", "Error message")
    if _handle_invalid_search_terms(search_by_make=False, search_by_model=False, search_by_year=False):
        return raise_error


create_search_button = tkinter.Button(m, text='Search Catalog', width=25, command=search_catalog)
create_search_button.grid(row=0)

exit_button = tkinter.Button(m, text='Exit', width=25, command=m.destroy)
exit_button.grid(row=10)

m.mainloop()
