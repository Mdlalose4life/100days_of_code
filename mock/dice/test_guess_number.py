import unittest
from unittest.mock import patch
from func import guess_number

@patch("func.roll_dice")
def test_guess_number(mock_roll_dice):
    mock_roll_dice.return_value = 2
    unittest.TestCase().assertEqual(guess_number(2), "You Won!")

if __name__ == '__main__':
    test_guess_number()