"""Test date."""

from magicbag import random_date, random_datetime, random_timestamp


def test_random_date():
    """Test random_date."""
    date = random_date()
    print("date:", date)


def test_random_datetime():
    """Test random_datetime."""
    datetime = random_datetime()
    print("datetime:", datetime)


def test_random_timestamp():
    """Test random_timestamp."""
    # set start from 1900 to test negative timestamp
    timestamp = random_timestamp(unit="s", start_year=1900)
    print("timestamp:", timestamp)
