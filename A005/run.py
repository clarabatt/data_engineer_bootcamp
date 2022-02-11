import datetime
from Curriculum import Curriculum
from Person import Person

clara = Person.Person(name='Clara', lastname='Battesini', birth_date=datetime.date(1995, 3, 17))

print(clara)
print(clara.name)
print(clara.age)

clara_curriculum = Curriculum.Curriculum(
    person=clara,
    experiences=['Studio Enzo', 'CPC', 'Cubos Tecnologia', 'Cubos Academy']
)

print(clara_curriculum)