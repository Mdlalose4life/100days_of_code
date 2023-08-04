import logging
import employee

logger = logging.getLogger(__name__)

logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')

file_handler = logging.FileHandler('test.log')

file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


def add(x, y):
    """Adds two numbers"""
    return x + y

def subtract(x, y):
    """Subtract the two numbers"""
    return x - y

def divide(x, y):
    """Devides to numbers"""
    return x / y

def multiply(x, y):
    """Multiply two numbers"""
    return x * y

x = 50
y = 5

add_num = add(x, y)
logger.debug("Add {} + {} = {}".format(x, y, add_num))

add_num = subtract(x, y)
logger.debug("Subtrac {} - {} = {}".format(x, y, add_num))

add_num = divide(x, y)
logger.debug("Divide {} / {} = {}".format(x, y, add_num))

add_num = multiply(x, y)
logger.debug("Multiply {} * {} = {}".format(x, y, add_num))