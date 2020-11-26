class VehicleBuilder:
    def __init__(self, make, model, year, mileage, price, color):
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage
        self.price = price
        self.color = color

    def values(self):
        return {
            'make': self.make,
            'model': self.model,
            'year': self.year,
            'mileage': self.mileage,
            'price': self.price,
            'color': self.color
        }
