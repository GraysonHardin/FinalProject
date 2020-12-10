import unittest
import datetime
from unittest.mock import patch, call, MagicMock

from main.csv_manager.monthly_sales_report import monthly_sales_report


class TestSalesReport(unittest.TestCase):
    @patch('main.csv_manager.monthly_sales_report.csv_writer')
    def test_csv_header(self, mock_csv_writer):
        monthly_sales_report(rows=[])

        mock_csv_writer.return_value.writerow.assert_called_with([
            'Vehicle ID',
            'Make',
            'Model',
            'Year',
            'Purchase Price',
            'Sold Price'
        ])

    @patch('main.csv_manager.monthly_sales_report.csv_writer')
    def test_csv_rows(self, mock_csv_writer):
        mock_csv_writer.return_value = MagicMock()
        rows = [{
            'id': '1',
            'make': 'Ford',
            'model': 'Mustang',
            'year': '2016',
            'purchase_price': '20000',
            'sell_price': '30000',
            'sold_date': datetime.date.today()
        }]

        monthly_sales_report(rows=rows)

        calls = [
            call(['Vehicle ID', 'Make', 'Model', 'Year', 'Purchase Price', 'Sold Price']),
            call(['1', 'Ford', 'Mustang', '2016', '20000', '30000'])
        ]

        mock_csv_writer.return_value.writerow.assert_has_calls(calls, any_order=False)

    @patch('main.csv_manager.monthly_sales_report.csv_writer')
    def test_csv_rows_shows_with_filtered_date_data(self, mock_csv_writer):
        mock_csv_writer.return_value = MagicMock()
        rows = [
            {
                'id': '1',
                'make': 'Ford',
                'model': 'Mustang',
                'year': '2016',
                'purchase_price': '20000',
                'sell_price': '30000',
                'sold_date': datetime.date.today()
            },
            {
                'id': '2',
                'make': 'Ford',
                'model': 'Mustang',
                'year': '2016',
                'purchase_price': '20000',
                'sell_price': '30000',
                'sold_date': datetime.date(2018, 12, 1)
            },
            {
                'id': '3',
                'make': 'Ford',
                'model': 'Mustang',
                'year': '2016',
                'purchase_price': '20000',
                'sell_price': '30000',
                'sold_date': ''
            }
        ]

        monthly_sales_report(rows=rows)

        calls = [
            call(['Vehicle ID', 'Make', 'Model', 'Year', 'Purchase Price', 'Sold Price']),
            call(['1', 'Ford', 'Mustang', '2016', '20000', '30000'])
        ]

        mock_csv_writer.return_value.writerow.assert_has_calls(calls, any_order=False)
        self.assertEqual(mock_csv_writer.return_value.writerow.call_count, 2)


if __name__ == '__main__':
    unittest.main()
