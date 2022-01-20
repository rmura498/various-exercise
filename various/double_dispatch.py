from abc import ABC, abstractmethod


class Character(ABC):

    def __init__(self, energy, ):
        self.energy = energy

    def __str__(self):
        return self.__class__.__name__

    @abstractmethod
    def team_up(self, other):
        pass

    @abstractmethod
    def _team_up_wizard(self, wizard):
        pass

    @abstractmethod
    def _team_up_elf(self, elf):
        pass

    @abstractmethod
    def _team_up_knight(self, knight):
        pass


class Wizard(Character):

    def __init__(self, energy):
        super().__init__(energy)

    # first dispatch
    def team_up(self, other):
        return other._team_up_wizard(self)

    # second dispatch
    def _team_up_wizard(self, wizard):
        return "now our strength is:", self.energy + wizard.energy

    def _team_up_elf(self, elf):
        return "We are not compatible"

    def _team_up_knight(self, knight):
        return "now our strength is:", self.energy + 2 * knight.energy


class Elf(Character):

    def __init__(self, energy):
        super().__init__(energy)

    # first dispatch
    def team_up(self, other):
        return other._team_up_elf(self)

    # second dispatch
    def _team_up_wizard(self, wizard):
        return "We are not compatible"

    def _team_up_elf(self, elf):
        return "now our strength is:", (self.energy + elf.energy) * 2

    def _team_up_knight(self, knight):
        return "now our strength is:", self.energy + 3 * knight.energy


class Knight(Character):

    def __init__(self, energy):
        super().__init__(energy)

    # first dispatch
    def team_up(self, other):
        return other._team_up_knight(self)

    # second dispatch
    def _team_up_wizard(self, wizard):
        return "now our strength is:", wizard.energy + 2 * self.energy

    def _team_up_elf(self, elf):
        return "now our strength is:", elf.energy + 3 * self.energy

    def _team_up_knight(self, knight):
        return "now our strength is:", self.energy + 3 * knight.energy



if __name__ == '__main__':
    print("\n\n")

    list_of_characters = [Wizard(10), Elf(20), Knight(30)]
    for t1 in list_of_characters:

        for t2 in list_of_characters:

            print(t1, 'and', t2, t1.team_up(t2))
