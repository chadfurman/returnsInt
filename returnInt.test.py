import unittest
from returnInt import returnsInt

class SimpleTest(unittest.TestCase):
    def testReturnIntReturnsInt(self):
        myInt = returnsInt()
        assert type(myInt) == type(str()), "return int must return int"

if __name__ == "__main__":
    unittest.main()
