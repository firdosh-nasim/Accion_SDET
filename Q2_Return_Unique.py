# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 18:48:31 2018

@author: firdo
"""


"""
2. Programming Challenge Description:
Write a function that accepts two arbitrary strings and returns a new string 
containing only the unique characters present in both inputs.
Input:
The function must accept two string parameters.
Output:
The function must return a string.
"""

import unittest
from collections import Counter

def return_unique(string1, string2):
    """
    Function Name: return_unique()
    
    Description: 
        Function accepts two arbitrary strings and returns a new string 
        containing only the unique characters present in both inputs.

    Args:
        string1: The first parameter.
        string2: The second parameter.

    Returns:
        string: The return value.

    """

    """
    Consdering two sets A and B, the unique elements between both the sets
    would be : (A union B) - (A intersection B)
    
    Similarly, we will convert both the input strings to Counter() dictionary 
    and perform the above operation
    """
    
    # Input type validation. Both the input must be of 'str' type
    if not (type(string1) == type(string2) == str):
        raise TypeError("Either one or both the input types are not valid")

    
    # Converting the given input string to Counter() dictionary
    string1_dict = Counter(string1)
    string2_dict = Counter(string2)
    
    # Find the union and intersection dictionaries
    string_union = string1_dict | string2_dict
    #print("string_union: ", string_union)
    string_intersection = string1_dict & string2_dict
    #print("string_intersection: ", string_intersection)
    
    # Take the difference
    string_union.subtract(string_intersection)
    
    # Form the result sring
    result_string = ''.join(list(string_union.elements()))
    #print("result_string: ", result_string)
    
    return result_string



class TestUniqueStringRoutine(unittest.TestCase):
    
    def test_1_happy_path(self):
        """
        Testcase to exercise positive test points
        """

        print(" Testing Positive Scenarios ".center(80, '*'))

        # Dictionary with the possible test points, in the form of
        # key : input argument value as tuple
        # value: expected result
        testcases = {
            # Overlapping characters 
            ('abcd', 'cdef'): 'abef',
            ('abcdxy', 'cdefst'): 'abxyefst',
            ('12345', '4567890'): '12367890',
            
            # Overlapping characters(repeatative)
            ('aaabcdd', 'cdeeef'): 'aaabdeeef',
            
            # Checking case sensitivity
            ('abcd', 'CDef'): 'abcdCDef',
            
            # No overlapping charaters
            ('abcd', 'efgh'): 'abcdefgh',
            
            # All overlapping charaters (duplicate string)
            ('abcd', 'abcd'): '',
            
            # One empty string
            ('abcd', ''): 'abcd',
            ('', 'efgh'): 'efgh',  
            
            # Both empty strings
            ('', ''): '',

        }

        # Iterate through the test points
        for input_val, expected_result in testcases.items():
            obtained_result = return_unique(*input_val)
            print(f"Testing with input: '{input_val}'."
                  f" Expecting: '{expected_result}'."
                  f" Obtained: '{obtained_result}'")

            self.assertEqual(expected_result, obtained_result)

        print('*' * 80)


    def test_2_exception(self):
        """
        Testcase to exercise exceptions
        """
        
        print(" Testing Exceptions ".center(80, '*'))
        
        # Testing scenario, without passing the input argument.
        # This is expected to throw a 'TypeError'
        print("Testing without providing all or one function argument")
        self.assertRaises(TypeError, return_unique)
        self.assertRaises(TypeError, return_unique, 'abcd')

        # Testing scenario, passing an integer input argument.
        # This is expected to throw a 'TypeError'
        print("Testing with passing integer argument, instead of string")
        self.assertRaises(TypeError, return_unique, 12345, 67890)
        self.assertRaises(TypeError, return_unique, 12345, '67890')
        self.assertRaises(TypeError, return_unique, '12345', 67890)
            
        print('*' * 80)
        

# main() routine to call the unit test
if __name__ == "__main__":
    unittest.main()
