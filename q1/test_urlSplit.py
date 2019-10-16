import unittest
from urlSplit import *

class test_urlSplit (unittest.TestCase):
	def test(self):
		# Assumptions : - The input should not be empty. 
		#				- The input should be in string format
		#				- The output is a list consisting of [protocol, Domain, Path]
		#				- If the input has multiple paths, then the path will be outputted as a string list with multiple paths. 
		# basic test
		test_cases = "ftp://bu.edu/"
		expected_output = ["ftp", "bu.edu", ""]
		split = urlSplit(test_cases)
		actual_output = split.urlSplitting()
		self.assertEqual(actual_output, expected_output, 'actual output must equal expected output')

		#with path 
		test_cases = "https://google.com/slides"
		expected_output = ["https", "google.com", "slides"]
		split = urlSplit(test_cases)
		actual_output = split.urlSplitting()
		self.assertEqual(actual_output, expected_output, 'actual output must equal expected output')


		#with path 
		test_cases = "https://www.google.com/some-path"
		expected_output = ["https", "www.google.com", "some-path"]
		split = urlSplit(test_cases)
		actual_output = split.urlSplitting()
		self.assertEqual(actual_output, expected_output, 'actual output must equal expected output')

		# Complicated Cases
		test_cases = "https://learn.bu.edu/bbcswebdav/pid-7388156-dt-content-rid-33552699_1/courses/19fallcascs591_c2/"
		expected_output = ["https", "learn.bu.edu", ["bbcswebdav", "pid-7388156-dt-content-rid-33552699_1","courses", "19fallcascs591_c2", ""]]
		split = urlSplit(test_cases)
		actual_output = split.urlSplitting()
		self.assertEqual(actual_output, expected_output, 'actual output must equal expected output')


		# Complicated Cases
		test_cases = "https://github.com/shoki5090/cs591_c2_assignment_5/blob/master/.gitignore"
		expected_output = ["https", "github.com", ["shoki5090", "cs591_c2_assignment_5","blob", "master", ".gitignore"]]
		split = urlSplit(test_cases)
		actual_output = split.urlSplitting()
		self.assertEqual(actual_output, expected_output, 'actual output must equal expected output')


if __name__ == '__main__':
	unittest.main()