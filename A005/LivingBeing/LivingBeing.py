import datetime
import math

class LivingBeing:
    '''
        It is a living being which needs a name and a birth date
    '''
    def __init__(self, name: str, birth_date: datetime.date) -> None:
        self.name = name
        self.birth_date = birth_date

    @property
    def age(self) -> int:
        '''
        return the person age, calculated by birth date
        '''
        return math.floor((datetime.date.today() - self.birth_date).days / 365.2425)

    def make_noise(self, noise: str):
        '''
        receive the noise and return a frase "{LivingBeing} made a noise: {the noise}"
        '''
        return print(f"{self.name} made a noise: {noise}")


class Dog(LivingBeing):
    '''
        A dog is a LivingBeing but also needs a breed
    '''
    def __init__(self, name: str, birth_date: datetime.date, breed: str) -> None:
        super().__init__(name, birth_date)
        self.breed = breed

    def __str__(self):
        return f"{self.name}'s breed is {self.breed} and they are {self.age} years"

    def bark(self):
        '''
        A dog makes a noise (bark): "Ruf ruf!"
        '''
        return self.make_noise("Ruf ruf!")