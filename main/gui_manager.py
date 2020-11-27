import tkinter
import tkinter as tk
from main.csv_manager.catalog import search

m = tkinter.Tk()
m.geometry('1920x1080')
m.title('Catalog')

# make input
# model input
# year input
# search(make, model, year)
# table grid to show results


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


create_search_button = tkinter.Button(m, text='Search Catalog', width=25, command=search_catalog)
create_search_button.grid(row=0)

exit_button = tkinter.Button(m, text='Exit', width=25, command=m.destroy)
exit_button.grid(row=10)

m.mainloop()
