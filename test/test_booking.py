import pytest

from airsorted import Booking, RoomBooking


def test_booking_dates():
    b = Booking('2015-06-01', '2015-06-05')
    assert [d for d in b.dates()] == ['2015-06-01', '2015-06-02', '2015-06-03', '2015-06-04', '2015-06-05']


def test_availability():
    dates = [{'start': '2016-06-01', 'end': '2016-06-15'}, {'start': '2016-07-01', 'end': '2016-07-15'},
             {'start': '2016-06-20', 'end': '2016-06-29'}]
    b = RoomBooking(dates)
    assert [d for d in b.availability(6)] == ['2016-06-16', '2016-06-17', '2016-06-18', '2016-06-19', '2016-06-30']


def test_double_booked():
    dates = [{'start': '2016-06-01', 'end': '2016-06-15'}, {'start': '2016-06-14', 'end': '2016-06-29'}]
    b = RoomBooking(dates)
    assert set([d for d in b.double_booked_days()]) == set(['2016-06-14', '2016-06-15'])
