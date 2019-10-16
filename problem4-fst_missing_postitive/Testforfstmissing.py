import unittest
from problem4 import*

class Testforfstmissing (unittest.TestCase):
  def testforfstmissing(self):
    input_list = [1,2,0]
    expect_output = 3
    actual_output = fst_missing(self, input_list)
    self.assertEqual(actual_output, expect_output, 'actual output must equal to the expect output')
    input_list = [3,4,-1,1]
    expect_output = 2
    actual_output = fst_missing(self, input_list)
    self.assertEqual(actual_output, expect_output, 'actual output must equal to the expect output')
    input_list = [7,8,9,11,12]
    expect_output = 1
    actual_output = fst_missing(self, input_list)
    self.assertEqual(actual_output, expect_output, 'actual output must equal to the expect output')
    input_list = [2]
    expect_output = 1
    actual_output = fst_missing(self, input_list)
    self.assertEqual(actual_output, expect_output, 'actual output must equal to the expect output')
    input_list = [1]
    expect_output = 2
    actual_output = fst_missing(self, input_list)
    self.assertEqual(actual_output, expect_output, 'actual output must equal to the expect output')
    input_list = [11,0,10,12,3,2]
    expect_output = 1
    actual_output = fst_missing(self, input_list)
    self.assertEqual(actual_output, expect_output, 'actual output must equal to the expect output')
  

if __name__ == '__main__':
        unittest.main()
