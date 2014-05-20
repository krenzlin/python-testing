import unittest
from mymodule import mean

class TestMymodule(unittest.TestCase):

    def test_mean(self):
        self.assertEqual(mean([10, 20]), 15)
        self.assertEqual(mean([100, 300]), 200)
        self.assertEqual(mean([1, 2]), 1.5)

 
if __name__ == '__main__':
    unittest.main()
