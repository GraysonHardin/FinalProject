import tkinter


def draw_table(new_window, rows):
    for i in range(len(rows)):
        column = 1
        for key in rows[i]:
            e = tkinter.Entry(new_window, width=20, fg='black', font=('Arial', 12, 'bold'))

            e.grid(row=i + 1, column=column)
            e.insert(tkinter.END, rows[i][key])
            column += 1
            e['state'] = tkinter.DISABLED


def draw_header(new_window, index, value):
    header = tkinter.Entry(new_window, width=20, fg='black', font=('Arial', 12, 'bold'))
    header.grid(row=0, column=index)
    header.insert(tkinter.END, value)
    header['state'] = tkinter.DISABLED
