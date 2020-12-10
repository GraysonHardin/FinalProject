import datetime


class PurchasedVehicleBuilder:
    def values(self, **kwargs):
        vehicle = {}
        for key, value in kwargs.items():
            if key == 'sold_date':
                vehicle.update({key: self._parse_to_date(date=value)})
            else:
                vehicle.update({key: value})

        return vehicle

    def _parse_to_date(self, date):
        if len(date) > 0:
            return datetime.datetime.strptime(date, '%Y-%m-%d').date()
        return date
