import csv
import locale
from main.vehicle_demos import VehicleDemos


def display_vehicle_make(vehicle_make, make):
    return f'Vehicle make is: {make[vehicle_make].make}'


def total_inventory_price_calculator(make):
    locale.setlocale(locale.LC_ALL, 'en_US')
    price_sum = 0
    for key in make:
        price_sum += int(make[key].price.replace(',', ''))
    return f'Total inventory price: {locale.format_string("%d", price_sum, grouping=True)}'


with open('vehicle_catalog.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0

    make = {}
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
            continue
        make[str(row[1])] = VehicleDemos(row[0], row[1], row[2], row[3], row[4], row[5])

    print(display_vehicle_make('Mustang', make))
    print(total_inventory_price_calculator(make))

