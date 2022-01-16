import unittest

from team_game import Wizard, Elf, Knight


class TestTeamMethods(unittest.TestCase):

    def setUp(self):
        self.wizard = Wizard('wizard')
        self.knight = Knight('knight')
        self.elf = Elf('elf')

    def test_team_up_k(self):
        self.wizard.team_up(self.knight)
        self.assertEqual(self.wizard.energy, self.knight.energy)

    def test_team_up_e(self):
        self.wizard.team_up(self.elf)
        self.assertNotEqual(self.wizard.energy, self.elf.energy)

    def test_team_up_w(self):
        wizard_two = Wizard('second')
        self.wizard.team_up(wizard_two)
        self.assertEqual(self.wizard.energy, wizard_two.energy)


suite = unittest.TestLoader().loadTestsFromTestCase(TestTeamMethods)
unittest.TextTestRunner().run(suite)