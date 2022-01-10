import datetime
from curriculum import Curriculum
from person import Person

clara = Person(name='Clara', lastname='Battesini', birth_date=datetime.date(1995, 3, 17))

print(clara)
print(clara.name)
print(clara.age)

clara_curriculum = Curriculum(
    person=clara,
    experiences=['Studio Enzo', 'CPC', 'Cubos Tecnologia', 'Cubos Academy']
)

print(clara_curriculum)