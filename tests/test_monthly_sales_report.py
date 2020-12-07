import unittest
from unittest.mock import patch, MagicMock

from main.csv_manager.monthly_sales_report import monthly_sales_report


class MyTestCase(unittest.TestCase):
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

    def test_csv_rows(self):
        rows = [{'id': '1', 'make': 'Ford'}]

        monthly_sales_report(rows=[])
        pass


if __name__ == '__main__':
    unittest.main()
