import unittest
from unittest.mock import patch

from main.csv_manager.load_data import get_csv_data


class TestLoadData(unittest.TestCase):
    @patch('main.csv_manager.load_data.open')
    @patch('main.csv_manager.load_data.reader')
    def test_call_open_with_correct_filename(self, mock_reader, mock_open):
        expected_reader = 'reader'
        expected_open = 'open'

        mock_reader.return_value = expected_reader
        mock_open.return_value = expected_open

        actual = get_csv_data()

        mock_open.assert_called_once_with('vehicle_catalog.csv')
        mock_reader.assert_called_with(expected_open, delimiter=',')
        self.assertEqual(actual, expected_reader)
