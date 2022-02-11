import Person

class Curriculum:
    '''
    Extends a person and give them profissional experiences
    '''
    def __init__(self, person: Person, experiences: list[str]):
        self.person = person
        self.experiences = experiences

    @property
    def experience_amount(self) -> int:
        '''
        Return the quantity of jobs experiences
        '''
        return len(self.experiences)

    @property
    def current_role(self) -> str:
        '''
        Return the current role
        '''
        return self.experiences[-1]

    def insert_experience(self, experience: str) -> None:
        '''
        Set a new experience
        '''
        self.experiences.append(experience)

    def __str__(self):
        return f"{self.person.name} {self.person.lastname} already worked for {self.experience_amount} companies in all their career. Now is working for {self.current_role}."
