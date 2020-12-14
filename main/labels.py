from tkinter import Label


# Extracted the labels (text that appears next to search fields) to a separate file to help keep gui_manager clean.
def draw_labels():
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
    add_vehicle_color_display_message = Label(text='Enter vehicle color')
    add_vehicle_paid_for_price_message = Label(text='Enter vehicle purchase price')
    add_vehicle_sold_for_price_message = Label(text='Enter vehicle sold price')
    add_vehicle_id_message = Label(text='Enter Vehicle ID')

    add_vehicle_make_display_message.grid(row=5, column=1)
    add_vehicle_model_display_message.grid(row=6, column=1)
    add_vehicle_year_display_message.grid(row=7, column=1)
    add_vehicle_mileage_display_message.grid(row=8, column=1)
    add_vehicle_color_display_message.grid(row=10, column=1)
    add_vehicle_paid_for_price_message.grid(row=11, column=1)
    add_vehicle_sold_for_price_message.grid(row=12, column=1)
    add_vehicle_id_message.grid(row=13, column=1)
