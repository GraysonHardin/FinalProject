import unittest
from unittest.mock import patch

from main.csv_manager.catalog import search

mocked_data = [
    ['Ford', 'Mustang', '2020', '5,000', '40,000', 'white'],
    ['Ford', 'Mustang', '2016', '30,000', '28,000', 'red'],
    ['Ford', 'F-150', '2012', '12,000', '70,000', 'black'],
    ['Honda', 'Civic', '2012', '100,000', '7,000', 'gray'],
    ['Honda', 'Accord', '2014', '80,000', '8,000', 'silver']
]


@patch('main.csv_manager.catalog.get_csv_data')
class TestSearchCatalog(unittest.TestCase):
    def test_search_catalog_by_make_model_and_year(self, mock_get_csv_data):
        mock_get_csv_data.return_value = mocked_data

        actual = search('Ford', 'Mustang', '2016')

        expected_row = {
            'make': 'Ford',
            'model': 'Mustang',
            'year': '2016',
            'mileage': '30,000',
            'price': '28,000',
            'color': 'red'
        }
        expected_row_length = 1

        self.assertEqual(len(actual), expected_row_length)
        self.assertListEqual(actual, [expected_row])

    def test_search_catalog_should_handle_no_make(self, _):
        with self.assertRaises(ValueError) as err:
            search(None, 'Mustang', '2016')

        self.assertTrue('Please provide make, model, and year.' in str(err.exception))

    def test_search_catalog_should_handle_no_model(self, _):
        with self.assertRaises(ValueError) as err:
            search('Ford', None, '2016')

        self.assertTrue('Please provide make, model, and year.' in str(err.exception))

    def test_search_catalog_should_handle_no_year(self, _):
        with self.assertRaises(ValueError) as err:
            search('Ford', 'Mustang', None)

        self.assertTrue('Please provide make, model, and year.' in str(err.exception))


if __name__ == '__main__':
    unittest.main()
