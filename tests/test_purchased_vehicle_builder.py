import unittest
from main.builders.purchased_vehicle_builder import PurchasedVehicleBuilder


class MyTestCase(unittest.TestCase):
    def test_constructor(self):
        builder = PurchasedVehicleBuilder(
            id='1',
            make='Ford',
            model='Mustang',
            year='2016',
            mileage='40,000',
            price='28,000',
            color='red',
            purchase_price='20,000',
            sell_price='25,000'
        )

        self.assertEqual(builder.id, '1')
        self.assertEqual(builder.make, 'Ford')
        self.assertEqual(builder.model, 'Mustang')
        self.assertEqual(builder.year, '2016')
        self.assertEqual(builder.mileage, '40,000')
        self.assertEqual(builder.price, '28,000')
        self.assertEqual(builder.color, 'red')
        self.assertEqual(builder.purchase_price, '20,000')
        self.assertEqual(builder.sell_price, '25,000')

    def test_values(self):
        builder = PurchasedVehicleBuilder(
            id='1',
            make='Ford',
            model='Mustang',
            year='2016',
            mileage='40,000',
            price='28,000',
            color='red',
            purchase_price='20,000',
            sell_price='25,000'
        )

        expected = {
            'id': '1',
            'make': 'Ford',
            'model': 'Mustang',
            'year': '2016',
            'mileage': '40,000',
            'price': '28,000',
            'color': 'red',
            'purchase_price': '20,000',
            'sell_price': '25,000'
        }

        self.assertEqual(builder.values(), expected)


if __name__ == '__main__':
    unittest.main()
