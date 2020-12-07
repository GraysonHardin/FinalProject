from main.csv_manager.csv_writer import csv_writer


def monthly_sales_report(rows):
    employee_writer = csv_writer()

    employee_writer.writerow(['Vehicle ID', 'Make', 'Model', 'Year', 'Purchase Price', 'Sold Price'])
    # for row in rows:
    #     employee_writer.writerow(
    #         [row['id'], row['make'], row['model'], row['year'], row['purchase_price'], row['sell_price']])
