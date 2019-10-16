import unittest
from unittest import mock
import area_and_perimeter

class Test_Area_Perimeter(unittest.TestCase):
	@mock.patch('area_and_perimeter.input', create=True)
	def test_area_perimeter(self, mocked_input):
		#testing circle
		inp = 'C'
		rad = 5
		mocked_input.side_effect = [str(rad)]
		expected_output = [78.5398,31.4159]
		actual_output = area_and_perimeter.find_area_perimeter(inp)
		self.assertEqual(actual_output, expected_output, 'actual output must equal expected output')
		#testing Rectangle
		inp = 'R'
		l = 5
		w = 3
		mocked_input.side_effect = [str(l), str(w)]
		expected_output = [15,16]
		actual_output = area_and_perimeter.find_area_perimeter(inp)
		self.assertEqual(actual_output, expected_output, 'actual output must equal expected output')
		#testing square
		inp = 'S'
		s = 5
		mocked_input.side_effect = [str(s)]
		expected_output = [25,20]
		actual_output = area_and_perimeter.find_area_perimeter(inp)
		self.assertEqual(actual_output, expected_output, 'actual output must equal expected output')
		#testing invalid shape input
		inp = 'g'
		mocked_input.side_effect = [str(s)]
		expected_output = 0
		actual_output = area_and_perimeter.find_area_perimeter(inp)
		self.assertEqual(actual_output, expected_output, 'actual output must equal expected output')


if __name__ == '__main__':
	unittest.main()
