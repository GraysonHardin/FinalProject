import tkinter
import tkinter as tk
from main.csv_manager.catalog import search


m = tkinter.Tk()
m.geometry('1280x720')
m.title('Catalog')

# make input
# model input
# year input
# search(make, model, year)
# table grid to show results


make_input = tk.Entry(m, width=70)
make_input.grid(row=2)


model_input = tk.Entry(m, width=70)
model_input.grid(row=3)

year_input = tk.Entry(m, width=70)
year_input.grid(row=4)


def search_catalog():
    search_results = search(make_input.get(), model_input.get(), year_input.get())
    print(search_results)

    draw_table(search_results, 2)


def draw_table(rows, grid_index):
    for i in range(len(rows)):
        e = tkinter.Entry(m, width=20, fg='black', font=('Arial', 12, 'bold'))

        e.grid(row=i, column=2)
        e.insert(tkinter.END, rows[i]['make'])

        model = tkinter.Entry(m, width=20, fg='black', font=('Arial', 12, 'bold'))
        model.grid(row=i, column=3)
        model.insert(tkinter.END, rows[i]['model'])

    # for i in range(len(rows)):
    #     for j in range(len(rows)):
    #         e = tkinter.Entry(m, width=20, fg='black', font=('Arial', 12, 'bold'))
    #         e.grid(row=i, column=j + grid_index)
    #         e.insert(tkinter.END, rows[i]['make'])




    # for i in range(total_rows):
    #     for j in range(total_columns):R
    #         e = tkinter.Entry(m, width=20, fg='black', font=('Arial', 12, 'bold'))
    #
    #         e.grid(row=i, column=j + column_index)
    #
    #         e.insert(tkinter.END, rows[i][j])
    #         e['state'] = tkinter.DISABLED


create_search_button = tkinter.Button(m, text='Search Catalog', width=60, command=search_catalog)
create_search_button.grid(row=1)

exit_button = tkinter.Button(m, text='Exit', width=60, command=m.destroy)
exit_button.grid(row=10)

m.mainloop()
