import unittest
from ..exponential_search import exponential_search

class Test_search(unittest.TestCase):

    def test_exponential_search(self):
        arr = [10, 20, 40, 45, 55]
        self.assertEquals(exponential_search(arr, 20, 1, len(arr)), 1)
        self.assertEquals(exponential_search(arr, 0, 1, len(arr)), -1)
        self.assertEquals(exponential_search(arr, 55, 1, len(arr)), 4)
        self.assertEquals(exponential_search(arr, 20000, 1, len(arr)), -1)

if __name__ == '__main__':
    unittest.main()