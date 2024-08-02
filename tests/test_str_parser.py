import datetime

from jrsync.utils import str_parser


def test_replace_standard_dates():
    res = str_parser.replace_dates(
        "test_{{DATE}}", datetime.datetime(year=2020, month=6, day=1)
    )

    assert res == "test_20200601"


def test_replace_date_in_the_past():
    res = str_parser.replace_dates(
        "test_{{DATE-1}}", datetime.datetime(year=2020, month=6, day=1)
    )

    assert res == "test_20200531"

def test_replace_date_in_the_future():
    res = str_parser.replace_dates(
        "test_{{DATE+1}}", datetime.datetime(year=2020, month=6, day=1)
    )

    assert res == "test_20200602"

def test_replace_date_in_the_future_with_spaces():
    res = str_parser.replace_dates(
        "test_{{DATE +  1}}", datetime.datetime(year=2020, month=6, day=1)
    )

    assert res == "test_20200602"