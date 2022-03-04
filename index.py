import unittest
import re

def Add(numbers):
    num_split = re.split(',|\n',numbers)
    if numbers == "":
        return "0"
    elif len(num_split) == 1:
        return numbers
    elif len(num_split) > 1:
        sum = 0
        for i in range(len(num_split)):
            sum += int(num_split[i])
        return str(sum)

class index(unittest.TestCase):
    def test_index_no_params(self):
        self.assertEqual(Add(""), "0")
        
    def test_index_one_param(self):
        self.assertEqual(Add("9"), "9")

    def test_index_two_params(self):
        self.assertEqual(Add("9, 10"), "19")

    def test_index_n_params(self):
        self.assertEqual(Add("40, 10, 20, 30, 50"), "150")

    def test_index_n_params(self):
        self.assertEqual(Add("40\n10,20,30,50"), "150")

if __name__ == '__main__':
    unittest.main()