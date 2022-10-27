from employee import Employee
import unittest

class TestEmployee(unittest.TestCase):

#the classes execute once in any programe start at end respectively
#setup and tear down function executes at testcase level
    @classmethod
    def setUpClass(cls): 
        print('setup class')


    @classmethod
    def tearDownClass(cls):
        print('tear down class')


    def setUp(self): #function that gives instructions to be executed beofore anything else
        self.emp2 = Employee('john', 'thuku')
        self.emp3 = Employee('naomi', 'njoki')


    def test_email(self):

        self.assertEqual(self.emp2.email, 'john.thuku@email.com')

        self.emp2.first = 'lucy'

        self.assertEqual(self.emp2.email, 'lucy.thuku@email.com')


    def test_fullname(self):

        
        self.assertEqual(self.emp3.fullname, 'naomi njoki')

        self.emp3.first = 'nao'
        self.assertEqual(self.emp3.fullname, "nao njoki")


    def tearDown(self):
        pass




if __name__ == '__main__':
    unittest.main()
