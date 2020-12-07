import tkinter as tk

from main.table_helpers import draw_table, draw_header


def open_inventory_table(m, rows):
    new_window = tk.Toplevel(m)
    new_window.title("Vehicle Inventory")
    new_window.geometry("1920x1080")

    draw_header(new_window, 1, 'ID')
    draw_header(new_window, 2, 'Make')
    draw_header(new_window, 3, 'Model')
    draw_header(new_window, 4, 'Year')
    draw_header(new_window, 5, 'Mileage')
    draw_header(new_window, 6, 'Color')
    draw_header(new_window, 7, 'Purchase Price')
    draw_header(new_window, 8, 'Sell Price')

    draw_table(new_window, rows)
