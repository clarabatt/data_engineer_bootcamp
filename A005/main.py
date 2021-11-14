import datetime
import math

class Person:
    def __init__(self, name: str, lastname: str, birth_date: datetime.date):
        self.name = name
        self.lastname = lastname
        self.birth_date = birth_date
    @property
    def age(self) -> int:
        return math.floor((datetime.date.today() - self.birth_date).days / 365.2425)
    def __str__ (self) -> str:
        return f"{self.name} {self.lastname} is {self.age}"

clara = Person(name='Clara', lastname='Battesini', birth_date=datetime.date(1995, 3, 17))

print(clara)
print(clara.name)
print(clara.age)