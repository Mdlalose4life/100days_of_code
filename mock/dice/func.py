#!/usr/bin/env python
from dice import roll_dice

def guess_number(num):
    result = roll_dice()
    if result == num:
        return "You Won!"
    else:
        return "You Lost"