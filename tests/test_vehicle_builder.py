import unittest
from main.csv_manager.vehicle_builder import VehicleBuilder


class MyTestCase(unittest.TestCase):
    def test_constructor(self):
        builder = VehicleBuilder(
            make='Ford',
            model='Mustang',
            year='2016',
            mileage='40,000',
            price='28,000',
            color='red'
        )

        self.assertEqual(builder.make, 'Ford')
        self.assertEqual(builder.model, 'Mustang')
        self.assertEqual(builder.year, '2016')
        self.assertEqual(builder.mileage, '40,000')
        self.assertEqual(builder.price, '28,000')
        self.assertEqual(builder.color, 'red')

    def test_values(self):
        builder = VehicleBuilder(
            make='Ford',
            model='Mustang',
            year='2016',
            mileage='40,000',
            price='28,000',
            color='red'
        )

        expected = {
            'make': 'Ford',
            'model': 'Mustang',
            'year': '2016',
            'mileage': '40,000',
            'price': '28,000',
            'color': 'red'
        }

        self.assertEqual(builder.values(), expected)


if __name__ == '__main__':
    unittest.main()
