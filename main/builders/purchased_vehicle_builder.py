import datetime


class PurchasedVehicleBuilder:
    def __init__(self, id, make, model, year, mileage, color, purchase_price, sell_price, sold_date):
        self.id = id
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage
        self.color = color
        self.purchase_price = purchase_price
        self.sell_price = sell_price
        self.sold_date = sold_date

    def values(self):
        return {
            'id': self.id,
            'make': self.make,
            'model': self.model,
            'year': self.year,
            'mileage': self.mileage,
            'color': self.color,
            'purchase_price': self.purchase_price,
            'sell_price': self.sell_price,
            'sold_date': self.parse_to_date()

        }

    def parse_to_date(self):
        if len(self.sold_date) > 0:
            return datetime.datetime.strptime(self.sold_date, '%Y-%m-%d').date()
        return self.sold_date
