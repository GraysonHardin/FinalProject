import tkinter as tk

from main.table_helpers import draw_table, draw_header


def open_catalog_table(m, rows):
    new_window = tk.Toplevel(m)
    new_window.title("Vehicle Catalog")
    new_window.geometry("900x900")

    draw_header(new_window, 1, 'Make')
    draw_header(new_window, 2, 'Model')
    draw_header(new_window, 3, 'Year')
    draw_header(new_window, 4, 'Mileage')
    draw_header(new_window, 5, 'Market Price')
    draw_header(new_window, 6, 'Color')

    draw_table(new_window, rows)
