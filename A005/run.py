import datetime
from Curriculum import Curriculum
from Person import Person
from LivingBeing import LivingBeing

clara = Person.Person(name='Clara', lastname='Battesini', birth_date=datetime.date(1995, 3, 17))

print(clara)
print(clara.name)
print(clara.age)

clara_curriculum = Curriculum.Curriculum(
    person=clara,
    experiences=['Studio Enzo', 'CPC', 'Cubos Tecnologia']
)

clara_curriculum.insert_experience("Cubos Academy")

print(clara_curriculum)

lola = LivingBeing.Dog(name="Lola", birth_date=datetime.date(2014, 10, 1), breed="SRD")

print(lola)
lola.bark()
