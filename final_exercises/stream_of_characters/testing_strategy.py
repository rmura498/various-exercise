import unittest

from main_strategy import Character
from strategy import StrategyUpper


class TestStrategyMethod(unittest.TestCase):

    def setUp(self):
        self.cls = Character()

    def test_printcharacterlower(self):
        character = 'A'
        self.assertTrue(self.cls.strategy.print_character(character).islower())

    def test_printcharacterupper(self):
        character = 'a'
        self.cls.strategy = StrategyUpper()
        self.assertTrue(self.cls.strategy.print_character(character).isupper())


suite = unittest.TestLoader().loadTestsFromTestCase(TestStrategyMethod)
unittest.TextTestRunner().run(suite)
