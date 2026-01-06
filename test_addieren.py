import unittest

def addiere(zahl1, zahl2):
    return zahl1 + zahl2

class TestAddiere(unittest.TestCase):
    def test_addiere(self):
        self.assertEqual(addiere(1, 2), 3)
        self.assertEqual(addiere(-1, 1), 0)
        self.assertEqual(addiere(0, 0), 0)

if __name__ == '__main__':
    unittest.main()