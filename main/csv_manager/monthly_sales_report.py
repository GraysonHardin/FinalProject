import datetime
import calendar

from main.csv_manager.csv_writer import csv_writer


def monthly_sales_report(rows):
    writer = csv_writer()

    writer.writerow(['Vehicle ID', 'Make', 'Model', 'Year', 'Purchase Price', 'Sold Price'])

    def is_within_date_range(value):
        year = datetime.datetime.now().year
        month = datetime.datetime.now().month
        date_range = calendar.monthrange(year, month)
        start = datetime.date(year, month, date_range[0])
        end = datetime.date(year, month, date_range[1])

        if isinstance(value['sold_date'], str):
            return False

        return start <= value['sold_date'] <= end

    filtered_rows = list(filter(is_within_date_range, rows))

    for row in filtered_rows:
        writer.writerow(
            [row['id'], row['make'], row['model'], row['year'], row['purchase_price'], row['sell_price']])
