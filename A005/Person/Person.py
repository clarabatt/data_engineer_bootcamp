import datetime
import math

class Person:
    '''
    Create a person who has a name, lastname and birth date
    '''
    def __init__(self, name: str, lastname: str, birth_date: datetime.date):
        self.name = name
        self.lastname = lastname
        self.birth_date = birth_date
    @property
    def age(self) -> int:
        '''
        return the person age, calculated by birth date
        '''
        return math.floor((datetime.date.today() - self.birth_date).days / 365.2425)
    def __str__ (self) -> str:
        return f"{self.name} {self.lastname} is {self.age}"
