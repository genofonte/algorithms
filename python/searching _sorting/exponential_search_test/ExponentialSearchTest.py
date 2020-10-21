from ..exponential_search import exponential_search
import unittest

class Test_search(unittest.TestCase):

    def exponential_search(self):
        arr = [10, 20, 40, 45, 55]
        self.assertEquals(exponential_search(arr, 20, 1, len(arr)),2)

if __name__ == '__main__':
    unittest.main()