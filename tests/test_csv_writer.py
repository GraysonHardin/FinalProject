import csv
import unittest
from unittest.mock import patch

from main.csv_manager.csv_writer import csv_writer


@patch('main.csv_manager.csv_writer.open')
@patch('main.csv_manager.csv_writer.writer')
class MyTestCase(unittest.TestCase):
    def test_csv_writer(self, mock_writer, mock_open):
        expected_writer = 'write'
        expected_opener = 'open'

        mock_writer.return_value = expected_writer
        mock_open.return_value = expected_opener

        actual = csv_writer()
        mock_writer.assert_called_with(expected_opener, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        mock_open.assert_called_once_with('../monthly_sales_report.csv', mode='w')
        self.assertEqual(actual, expected_writer)


if __name__ == '__main__':
    unittest.main()
