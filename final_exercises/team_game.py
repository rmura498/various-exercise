from abc import ABC, abstractmethod


class Character(ABC):

    @abstractmethod
    def __init__(self, name, energy):
        pass

    @abstractmethod
    def team_up(self, another):
        pass

    @abstractmethod
    def wizard_team_up(self, another):
        pass

    @abstractmethod
    def elf_team_up(self, another):
        pass

    @abstractmethod
    def knight_team_up(self, another):
        pass


class Wizard(Character):

    def __init__(self, name, energy=3):
        self.name = name
        self.energy = energy

    def team_up(self, another):
        another.wizard_team_up(self)

    def wizard_team_up(self, another):
        energy = self.energy + another.energy
        self.energy = energy
        another.energy = energy
        print("Now we have double energy")

    def elf_team_up(self, another):
        print("we are not compatible")

    def knight_team_up(self, another):
        energy = self.energy + 2 * another.energy
        self.energy = energy
        another.energy = energy
        print("We are too strong")


class Elf(Character):

    def __init__(self, name, energy=5):
        self.name = name
        self.energy = energy

    def team_up(self, another):
        another.elf_team_up(self)

    def wizard_team_up(self, another):
        print("we are not compatible")

    def elf_team_up(self, another):
        self.energy += another.energy + 10
        another.energy += self.energy + 10
        print("Now we have double energy plus ten")

    def knight_team_up(self, another):
        self.energy += 2 * another.energy
        another.energy = another.energy * 2 + self.energy
        print("We are too strong")


class Knight(Character):

    def __init__(self, name, energy=1):
        self.name = name
        self.energy = energy

    def team_up(self, another):
        another.knight_team_up(self)

    def wizard_team_up(self, another):
        energy = self.energy + 2 * another.energy
        self.energy = energy
        another.energy = energy
        print("We are too strong")

    def elf_team_up(self, another):
        self.energy += 2 * another.energy
        another.energy = another.energy * 2 + self.energy
        print("We are too strong")

    def knight_team_up(self, another):
        self.energy += another.energy + 20
        another.energy += self.energy + 20
        print("Now we have double energy plus 20")


wizard = Wizard('chicco')
knight = Knight('puddu')
elf = Elf('willy')

wizard.team_up(knight)
