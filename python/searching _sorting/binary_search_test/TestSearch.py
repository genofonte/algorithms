from ..binary_search import search
import unittest


class TestSearch(unittest.TestCase):

    def bin_search(self):
        self.assertEqual(search([1, 2], 1), 1)
        self.assertEqual(search([1, 2, 3], 1), 1)


if __name__ == '__main__':
    unittest.main()
