import unittest
from core import spliter


class TestSpliter(unittest.TestCase):

    def test_sentence(self):
        self.assertEqual(spliter(["ala ma kota"]), ['Ala 3', 'Ma 2', 'Kota 4'])


if __name__ == '__main__':
    unittest.main()
