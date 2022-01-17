import unittest
from ex3 import PiggyBank
from unittest.mock import patch


class TestPiggyBank(unittest.TestCase):

    def setUp(self):
        self.cls = PiggyBank(30)

    def test_retrieve(self):
        value = self.cls.total_amount + 10
        self.assertFalse(self.cls.retrieve(value))
        value = self.cls.total_amount - 10
        self.assertTrue(self.cls.retrieve(value))

    def test_save(self):
        value = 10
        init_total_amount = self.cls.total_amount
        self.cls.save(value)
        self.assertEqual(self.cls.total_amount, init_total_amount + value)


suite = unittest.TestLoader().loadTestsFromTestCase(TestPiggyBank)
unittest.TextTestRunner().run(suite)
