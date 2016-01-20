from datetime import datetime, timedelta
from calendar import monthrange
from itertools import chain
from collections import Counter

class Booking:

    def __init__(self, start, end):
        self.start = start
        self.end = end

    def dates(self):
        start = datetime.strptime(self.start, '%Y-%m-%d').date()
        end = datetime.strptime(self.end, '%Y-%m-%d').date()

        while start + timedelta(days=1) <= end:
            yield start.isoformat()
            start += timedelta(days=1)
        yield end.isoformat()



class RoomBooking:

    def __init__(self, bookings):
        self.bookings = [Booking(b['start'], b['end']) for b in bookings]

    def double_booked_days(self):
        booked_days = Counter([d for d in chain(*[b.dates() for b in self.bookings])])
        for k, v in booked_days.items():
            if v == 2:
                yield k

    def availability(self, month, year=datetime.now().year):
        start = datetime(year, int(month), 1).date().isoformat()
        end_month = monthrange(year, int(month))[1]
        end = datetime(year, int(month), end_month).date().isoformat()
        # reuse the booking class
        availability = Booking(start, end)
        booked_days = [d for d in chain(*[b.dates() for b in self.bookings])]
        for available_day in availability.dates():
            if available_day not in booked_days:
                yield available_day


def main():
    dates = [{'start': '2016-06-01', 'end': '2016-06-15'}, {'start': '2016-07-01', 'end': '2016-07-15'},
             {'start': '2016-06-20', 'end': '2016-06-29'}]
    r = RoomBooking(dates)
    month = input('insert month in number format (1-12): ')
    avaiability = r.availability(month)
    for d in avaiability:
        print(d)

if __name__ == '__main__':
    main()
