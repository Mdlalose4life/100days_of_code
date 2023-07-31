#!/usr/bin/env python
import datetime
from unittest.mock import Mock

sunday = datetime.datetime(year=2023, month=7, day=29)
monday = datetime.datetime(year=203, month=7, day=30)

datetime = Mock()

def is_weekday():
    today = datetime.datetime.today()
    return (0 <= today.weekday() < 5)


datetime.datetime.today.return_value = monday

assert is_weekday()

datetime.datetime.today.return_value = sunday

assert not is_weekday()