import pytest
from datetime import datetime
from main import date


@pytest.fixture
def current_datetime():
    return datetime(2020, 1, 1)


def test_set_date_time(current_datetime):
    assert current_datetime == datetime(
        2020, 1, 1
    ), "current_datetime should return the fixed datetime 2020-01-01"


def test_current_date_time():
    result = date()
    assert isinstance(result, datetime), "The function should return a datetime object"
