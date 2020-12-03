import tkinter
import tkinter as tk


def open_table_window(m, rows):
    new_window = tk.Toplevel(m)
    new_window.title("New Window")
    new_window.geometry("1080x480")
    _draw_table(new_window, rows)


def _draw_table(new_window, rows):
    for i in range(len(rows)):
        column = 3
        for key in rows[i]:
            e = tkinter.Entry(new_window, width=20, fg='black', font=('Arial', 12, 'bold'))

            e.grid(row=i, column=column)
            e.insert(tkinter.END, rows[i][key])
            column += 1
            e['state'] = tkinter.DISABLED
