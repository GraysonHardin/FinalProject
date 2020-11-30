import tkinter
import tkinter as tk
from main.csv_manager.catalog import search
from main.csv_manager.vehicle_builder import VehicleBuilder
from tkinter import messagebox
from tkinter import *

m = tkinter.Tk()
m.geometry('1920x1080')
m.title('Catalog')


display_make_input_message = Label(text='Enter vehicle make')
display_model_input_message = Label(text='Enter vehicle model')
display_year_input_message = Label(text='Enter vehicle year')

display_make_input_message.grid(row=1, column=1)
display_model_input_message.grid(row=2, column=1)
display_year_input_message.grid(row=3, column=1)

catalog_searcher = VehicleBuilder

make_input = tk.Entry(m, width=25)
make_input.grid(row=1, column=2)

model_input = tk.Entry(m, width=25)
model_input.grid(row=2, column=2)

year_input = tk.Entry(m, width=25)
year_input.grid(row=3, column=2)


def search_catalog():
    search_results = search(make_input.get(), model_input.get(), year_input.get())
    print(search_results)
    draw_table(search_results)
    model_input.delete(0, tk.END)
    make_input.delete(0, tk.END)
    year_input.delete(0, tk.END)


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

exit_button = tkinter.Button(m, text='Exit', width=25, command=m.destroy)
exit_button.grid(row=10, column=2)

m.mainloop()
