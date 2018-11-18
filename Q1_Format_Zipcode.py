# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 18:35:06 2018

@author: firdo
"""

import unittest

"""
Below is the function under test
"""


def format_zipcode(zip_code):
    if len(zip_code) <= 5:
        return '{:>05}'.format(zip_code)

    if len(zip_code) == 10:
        return str(zip_code)

    if len(zip_code) == 9:
        return '{}-{}'.format(zip_code[:5], zip_code[5:])


"""
Below is the unit testing class
"""


class TestZipCode(unittest.TestCase):
    def test_1_happy_path(self):
        """
        Testcase to exercise positive test points
        """

        print(" Testing Positive Scenarios ".center(80, '*'))

        # Dictionary with the possible test points, in the form of
        # key : input argument value
        # value: expected result
        testcases = {
            # Below 4 tests to exercise the condition len(zip_code) <= 5
            '': '00000',
            '1': '00001',
            '1234': '01234',
            '12345': '12345',

            # Below test to exercise the condition len(zip_code) == 10
            '1234567890': '1234567890',

            # Below test to exercise the condition len(zip_code) == 9
            '123456789': '12345-6789',

        }

        # Iterate through the test points
        for input_val, expected_result in testcases.items():
            obtained_result = format_zipcode(input_val)
            print(f"Testing with input: '{input_val}'."
                  f"Expecting: '{expected_result}'."
                  f"Obtained: '{obtained_result}'")

            self.assertEqual(expected_result, obtained_result)

        print('*' * 80)

    def test_2_unhandled_inputs(self):
        """
        Testcase to exercise unhandled test input scenarios
        """

        print(" Testing Unhandled Input Scenarios ".center(80, '*'))

        # Dictionary with the possible test points, in the form of
        # key : input argument value
        # value: expected result
        testcases = {
            # When 6 <= len(zip_code) <= 8.
            # Considering only boundaries, i.e. 6 & 8
            '123456': None,
            '12345678': None,

            # When len(zip_code) > 10
            # Considering only boundaries, i.e. 11
            '12345678901': None,

        }

        # Iterate through the test points
        for input_val, expected_result in testcases.items():
            obtained_result = format_zipcode(input_val)
            print(f"Testing with input: '{input_val}'."
                  f"Expecting: '{expected_result}'." 
                  f"Obtained: '{obtained_result}'")

            self.assertEqual(expected_result, obtained_result)

        print('*' * 80)

    def test_3_special_char_inputs(self):
        """
        Testcase to exercise special character input values
        Note: The function under test will give us the output, as there is no
              check whether the given input in valid or not
        """

        print(" Testing Special Char Input Scenarios ".center(80, '*'))

        # Dictionary with the possible test points, in the form of
        # key : input argument value
        # value: expected result
        testcases = {
            # 9 '-' will return 10 '-'
            '---------': '----------',
            # @#$%^
            '@#$%': '0@#$%'

        }

        # Iterate through the test points
        for input_val, expected_result in testcases.items():
            obtained_result = format_zipcode(input_val)
            print(f"Testing with input: '{input_val}'."
                  f"Expecting: '{expected_result}'."
                  f"Obtained: '{obtained_result}'")

            self.assertEqual(expected_result, obtained_result)

        print('*' * 80)

    def test_4_exception(self):
        """
        Testcase to exercise exceptions
        """
        # Testing scenario, without passing the input argument.
        # This is expected to throw a 'TypeError'
        print(" Testing Exceptions ".center(80, '*'))

        print("Testing without providing the function argument")
        self.assertRaises(TypeError, format_zipcode)
        print('*' * 80)


if __name__ == "__main__":
    unittest.main()
