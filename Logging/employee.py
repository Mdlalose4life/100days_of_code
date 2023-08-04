import logging

logger = logging.getLogger(__name__)

logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(levelname)s:%(name)s:%(message)s')

file_handler = logging.FileHandler('employee.log')

file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


class Employee:
    """                                                                                                                                                                                                                                                                                                                                                                                                                                     
    An emplyoyee class
    """
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

        logger.info('Employee is: {} - {}'.format(self.name, self.surname))

    @property
    def email(self):
        return '{}.{}@gmail.com'.format(self.name, self.surname)

    @property
    def fullname(self):
        return '{}.{}'.format(self.name, self.surname)

emplyoyee1 = Employee('Sbusiso', 'Mdlalose')
emplyoyee2 = Employee('Senzo', 'Meyiwa')
emplyoyee3 = Employee('Vusi', 'Zwane')