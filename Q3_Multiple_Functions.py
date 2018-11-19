# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 18:50:53 2018

@author: firdo
"""

"""
3. Programming Challenge Description:
Write 4 functions based on the following requirements

a. Write a function that accepts an integer and returns True if the input is 
between 4 and 10, inclusive; otherwise, return False

b. Write a function to test if a list contains any items. Return 'EMPTY' if it 
does not contain any items and 'NOT EMPTY' if it does.

c. Write a function that accepts a file name and a string and writes the string
 to the file with the given file name.
 
d. Write a function that accepts a list and doubles each value in the list. 
When no input parameter is provided, return an empty list.

Input:
N/A
Output:
N/A
"""

import unittest
import sys
import os

"""
a. Write a function that accepts an integer and returns True if the input is 
between 4 and 10, inclusive; otherwise, return False
"""
def check_integer_range(in_num):
    
    try:
        result =  (4 <= in_num <= 10)
    except:
            raise sys.exc_info()[0]("Given input is not an 'int'")
    else:
        return result
 
"""
b. Write a function to test if a list contains any items. Return 'EMPTY' if it 
does not contain any items and 'NOT EMPTY' if it does.
"""
def check_list(in_list):
    
    # Input type validation. Input must be a 'list'
    if not (type(in_list) == list):
        raise TypeError("Given input is not a 'list'")
        
    return "NOT EMPTY" if in_list  else "EMPTY"

"""
c. Write a function that accepts a file name and a string and writes the string
 to the file with the given file name.
"""
def write_to_file(in_filename, in_string):
    
    # As per the requirement, the function should take only string input.
    # Therefore checking for the same
    if not (type(in_string) == str):
        raise TypeError("Given input is not a 'string'")
        
    try:
        with open (in_filename, 'w') as file_handle:
            file_handle.write(in_string)
    except:
            raise sys.exc_info()[0](sys.exc_info()[1])
    else: 
        return True

"""
d. Write a function that accepts a list and doubles each value in the list. 
When no input parameter is provided, return an empty list.
"""
def double_list_elements(in_list = None):
    
    # Return empty list, no parameter provided
    if not in_list:
        return []
    
    # Input type validation. Input must be a 'list'
    elif not (type(in_list) == list):
        raise TypeError("Given input is not a 'list'")
    
    # Valid list
    else:
        return list(map(lambda x: 2*x, in_list))
   
    
class TestMultipleFunctions(unittest.TestCase):
    
    def test_1_check_integer_range(self):
        """
        Testcase to test check_integer_range()
        """

        print(" Testing check_integer_range() ".center(80, '*'))

        # Dictionary with the possible test points, in the form of
        # key : input argument value 
        # value: expected result
        testcases = {
            # Checking with values between 4 & 10 (both inclusive)
            4: True,
            10: True,
            8: True,
            
            # Values outside the range
            3: False,
            11: False,
            
            # Max integer value
            sys.maxsize: False,
            
            # Checking extremes ( -infinity & +infinity)
            float('inf'): False,
            float('-inf'): False,
            
            # Invalid number: NaN
            float('nan'): False,
        }

        # Iterate through the test points
        for input_val, expected_result in testcases.items():
            obtained_result = check_integer_range(input_val)
            print(f"Testing with input: '{input_val}'."
                  f" Expecting: '{expected_result}'."
                  f" Obtained: '{obtained_result}'")

            self.assertEqual(expected_result, obtained_result)

        # Non-Numeric input
        print("Testing with Non-Numeric argument")
        self.assertRaises(TypeError, check_integer_range, 'aa')
        
        # Without argument
        print("Testing without providing all or one function argument")
        self.assertRaises(TypeError, check_integer_range)

        print('*' * 80)

    def test_2_check_list(self):
        """
        Testcase to test check_list()
        """

        print(" Testing check_list() ".center(80, '*'))

        # List with the possible test points, in the form of
        # Even index : input argument value 
        # Odd index: expected result
        testcases = [
            # Checking with empty list
            [], 'EMPTY',
            
            # Checking with non-empty list
            [1], 'NOT EMPTY',
            [1, 2, 3, 4], 'NOT EMPTY',
            ['a', 'b', 'c', 'd'], 'NOT EMPTY', 

        ]

        # Iterate through the test points
        for idx  in range(0, len(testcases), 2):
            input_val = testcases[idx]
            expected_result = testcases[idx + 1]
            obtained_result = check_list(input_val)
            print(f"Testing with input: '{input_val}'."
                  f" Expecting: '{expected_result}'."
                  f" Obtained: '{obtained_result}'")

            self.assertEqual(expected_result, obtained_result)

        
        # Non-Numeric input
        print("Testing with Non-List argument")
        self.assertRaises(TypeError, check_list, 'aa')
        
        # Without argument
        print("Testing without providing all or one function argument")
        self.assertRaises(TypeError, check_list)
        
        print('*' * 80)

    def test_3_write_to_file(self):
        """
        Testcase to test write_to_file()
        """

        print(" Testing write_to_file() ".center(80, '*'))
        
        """
        Positive Testcases
        """
        # Valid file at current folder and valid input string
        file_name = 'sample.txt'
        in_string = "Valid file at current folder and valid input string"
        print(f"Testing with file: '{file_name}' and  string: '{in_string}'")
        self.assertTrue(write_to_file(file_name, in_string))
        
        # Overwrting an existing file. File was created in previous testcase
        file_name = 'sample.txt'
        in_string = "Overwrting an existing file. File was created in previous testcase"
        print(f"Testing with file: '{file_name}' and  string: '{in_string}'")
        self.assertTrue(write_to_file(file_name, in_string))
        
        # Valid file at differnt folder and valid input string
        # Note: Plese have the directory created
        file_name = os.path.join('sample_folder', 'sample.txt')
        in_string = "Valid file at differnt folder and valid input string"
        print(f"Testing with file: '{file_name}' and  string: '{in_string}'")
        self.assertTrue(write_to_file(file_name, in_string))

        """
        Negative Testcases
        """
        # Valid file at current folder and  non-string input
        file_name = 'sample.txt'
        in_string = 12345
        print(f"Testing with file: '{file_name}' and  non-string input: {in_string}")
        self.assertRaises(TypeError, write_to_file, file_name, in_string)

        # File at non-exiting folder
        file_name = os.path.join('non_existing_folder', 'sample.txt')
        in_string = "This will throw an exception: FileNotFoundError"
        print(f"Testing with file: '{file_name}' and  non-string input: {in_string}")
        self.assertRaises(FileNotFoundError, write_to_file, file_name, in_string)

        # Writing to a hidden file at current folder
        # Note: Please create a hidden file named 'hidden_file.txt'
        file_name = 'hidden_file.txt'
        in_string = "This will throw an exception: PermissionError"
        print(f"Testing with file: '{file_name}' and  non-string input: {in_string}")
        self.assertRaises(PermissionError, write_to_file, file_name, in_string)
        
        # Writing to a readonly file at current folder
        # Note: Please create a read-only file 'readonly_file.txt'
        file_name = 'readonly_file.txt'
        in_string = "This will throw an exception: PermissionError"
        print(f"Testing with file: '{file_name}' and  non-string input: {in_string}")
        self.assertRaises(PermissionError, write_to_file, file_name, in_string)

        
        print('*' * 80)

    def test_4_double_list_elements(self):
        """
        Testcase to test double_list_elements()
        """

        print(" Testing double_list_elements() ".center(80, '*'))

        # List with the possible test points, in the form of
        # Even index : input argument value 
        # Odd index: expected result
        testcases = [
            # Checking with empty list
            [], [],
            
            # Checking with non-empty list
            [1], [2],
            [1, 2, 3, 4], [2, 4, 6, 8],
            [-11, -22, -33, -44], [-22, -44, -66, -88],
            ['a', 'b', 'c', 'd'], ['aa', 'bb', 'cc', 'dd'], 
            [1, 2, 'x', 'y'], [2, 4, 'xx', 'yy'],
            
            # Nested List
            [1, 2, [11, 22]], [2, 4, [11, 22, 11, 22]],
            
            # Nested list with a tuple
            [1, 2, (11, 22), 4], [2, 4, (11, 22, 11, 22), 8],
                    
            # Checking with 'None'
            None, [],
            
        ]

        # Iterate through the test points
        for idx  in range(0, len(testcases), 2):
            input_val = testcases[idx]
            expected_result = testcases[idx + 1]
            obtained_result = double_list_elements(input_val)
            print(f"Testing with input: '{input_val}'."
                  f" Expecting: '{expected_result}'."
                  f" Obtained: '{obtained_result}'")

            self.assertEqual(expected_result, obtained_result)
        
        # Without argument
        expected_result = []
        obtained_result = double_list_elements()
        print(f"Testing without input."
              f" Expecting: '{expected_result}'."
              f" Obtained: '{obtained_result}'")

        self.assertEqual(expected_result, obtained_result)
               
        # Non-Numeric input
        print("Testing with Non-List argument")
        self.assertRaises(TypeError, double_list_elements, 'aa')
        
        # Nested list with dictionary
        print("Testing with Nested list with dictionary")
        self.assertRaises(TypeError, double_list_elements, [1, {'a': 11}, 3])

        # Nested list with set
        print("Testing with Nested list with set")
        self.assertRaises(TypeError, double_list_elements, [1, {2, 3}, 4])
        
        print('*' * 80)
    
# Driver function
if __name__ == "__main__":

    unittest.main()



