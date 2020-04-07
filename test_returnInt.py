import unittest
from returnInt import returnsInt


class SimpleTest(unittest.TestCase):
    def testReturnIntReturnsInt(self):
        myInt = returnsInt()
        assert type(myInt) == type(int()), "return int must return int"


if __name__ == "__main__":
    unittest.main()
