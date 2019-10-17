#Author: Masayoshi Iwasa
#Class: CS591

import problem3
import unittest

class Test_P3(unittest.TestCase):
	"""Test for Assignment 5 Problem 3: Multiply two numbers in strings"""
	def test_problem3(self):
		# Assumptions : - The input should not be empty. 
		#				- The input should be in string format
		#				- The input must have two numbers
		#				- The output is number (input1 * input2)

		# basic test
		test_num1 = '4'
		test_num2 = '8'
		expected_output = '32'
		actual_output = problem3.multiply_string_nums(test_num1, test_num2)
		self.assertEqual(actual_output, expected_output, 'actual output must equal expected output')

		# test with 0
		test_num1 = '0'
		test_num2 = '20'
		expected_output = '0'
		actual_output = problem3.multiply_string_nums(test_num1, test_num2)
		self.assertEqual(actual_output, expected_output, 'actual output must equal expected output')


		# test with large numbers
		test_num1 = '80000'
		test_num2 = '500'
		expected_output = '40000000'
		actual_output = problem3.multiply_string_nums(test_num1, test_num2)
		self.assertEqual(actual_output, expected_output, 'actual output must equal expected output')

		# test with small and large numbers
		test_num1 = '2'
		test_num2 = '50000'
		expected_output = '100000'
		actual_output = problem3.multiply_string_nums(test_num1, test_num2)
		self.assertEqual(actual_output, expected_output, 'actual output must equal expected output')


		# test with same numbers
		test_num1 = '5'
		test_num2 = '5'
		expected_output = '25'
		actual_output = problem3.multiply_string_nums(test_num1, test_num2)
		self.assertEqual(actual_output, expected_output, 'actual output must equal expected output')

if __name__ == '__main__':
	unittest.main()