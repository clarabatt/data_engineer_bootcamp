from person import Person

class Curriculum:
    def __init__(self, person: Person, experiences: list[str]):
        self.person = person
        self.experiences = experiences

    @property
    def experience_amount(self) -> int:
        return len(self.experiences)

    @property
    def current_role(self) -> str:
        return self.experiences[-1]
