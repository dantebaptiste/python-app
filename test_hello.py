import hello as hi
import unittest

class Test(unittest.TestCase):
    #1
    def test_hello_Jaquline(self):
        print("test_hello_Jaquline")
        name1 = "Jaquline"
        self.assertEqual(hi.hello(name1), "Hello, Jaqulin")

    #2
    def test_hello_Blake(self):
        print("test_hello_Blake")
        name2 = "Blake"
        self.assertEqual(hi.hello(name2), "Hello, Blak")

if __name__ == '__main__':
    unittest.main()
