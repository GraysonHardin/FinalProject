import tkinter as tk

from main.table_helpers import draw_table, draw_header


# This handles the catalog table (also known as the market value searcher)
def open_catalog_table(m, rows):
    new_window = tk.Toplevel(m)
    new_window.title('Vehicle Market Value')
    new_window.geometry('1200x1000')

    draw_header(new_window, 1, 'Make')
    draw_header(new_window, 2, 'Model')
    draw_header(new_window, 3, 'Year')
    draw_header(new_window, 4, 'Mileage')
    draw_header(new_window, 5, 'Market Price')
    draw_header(new_window, 6, 'Color')

    draw_table(new_window, rows)
