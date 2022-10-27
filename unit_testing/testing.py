import base
import unittest

class TestBase(unittest.TestCase):
    def test_add(self):
        #results = base.add(10, 15)
        self.assertEqual(base.add(10, 15), 25)


    def test_subtract(self):
        #results = base.add(10, 15)
        self.assertEqual(base.subtract(10, 15), -5)


    def test_multiply(self):
        #results = base.add(10, 15)
        self.assertEqual(base.multiply(10, 15), 150)

        
    def test_divide(self):
        #results = base.add(10, 15)
        self.assertEqual(base.divide(10, 2), 5)

        self.assertRaises(ValueError, base.divide, 10, 0 )





if __name__ == '__main__':
    unittest.main()