class PurchasedVehicleBuilder:
    def __init__(self, id, make, model, year, mileage, color, purchase_price, sell_price):
        self.id = id
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage
        self.color = color
        self.purchase_price = purchase_price
        self.sell_price = sell_price

    def values(self):
        return {
            'id': self.id,
            'make': self.make,
            'model': self.model,
            'year': self.year,
            'mileage': self.mileage,
            'color': self.color,
            'purchase_price': self.purchase_price,
            'sell_price': self.sell_price

        }