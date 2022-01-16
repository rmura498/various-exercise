import unittest
from testing import Prova


class TestcodeMethods(unittest.TestCase):

    def setUp(self):
        self.v1 = 1
        self.v2 = 2
        self.cls = Prova()

    def test_init(self):
        self.assertTrue(self.cls.v1 == 0)
        self.assertTrue(self.cls.v2 == 0)

    def test_sum(self):

        self.cls.v1 = self.v1
        self.cls.v2 = self.v2

        self.assertEqual(self.cls.sum(), self.v1+self.v2)


suite = unittest.TestLoader().loadTestsFromTestCase(TestcodeMethods)
unittest.TextTestRunner().run(suite)
