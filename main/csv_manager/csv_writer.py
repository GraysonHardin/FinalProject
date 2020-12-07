from csv import writer
import csv


def csv_writer():
    open_csv_writer = open('../monthly_sales_report.csv', mode='w')

    return writer(open_csv_writer, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
