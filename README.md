# Accion_SDET
Solution for Python SDET Hirevue

IMPORTANT NOTE:
---------------
For all the testcase/scripts to work, please do the following before executing them
1. Create/make a file "readonly_file.txt" and make it READ ONLY
2. Create/make a file "hidden_file.txt" and make it HIDDEN
3. Create/copy a folder "sample_folder"


# The repository contains the following files
---------------------------------------------
C:\Backup\INSOFE\OneDrive\Accion_Rackspace\git_copy\Accion_SDET>dir
 Volume in drive C is Windows
 Volume Serial Number is 7264-D945

 Directory of C:\Backup\INSOFE\OneDrive\Accion_Rackspace\git_copy\Accion_SDET

19-11-2018  16:28    <DIR>          .
19-11-2018  16:28    <DIR>          ..
18-11-2018  19:48             4,493 Q1_Format_Zipcode.py
18-11-2018  20:28             4,634 Q2_Return_Unique.py
19-11-2018  11:38            11,104 Q3_Multiple_Functions.py
19-11-2018  16:19             8,200 Q4_OO_Excercise.py
19-11-2018  16:25             8,389 README.md
19-11-2018  11:35                 0 readonly_file.txt
19-11-2018  11:14    <DIR>          sample_folder
               6 File(s)         36,820 bytes
               3 Dir(s)  334,430,023,680 bytes free

C:\Backup\INSOFE\OneDrive\Accion_Rackspace\git_copy\Accion_SDET>



# Execution Result
------------------
C:\Backup\INSOFE\OneDrive\Accion_Rackspace\git_copy\Accion_SDET>python Q1_Format_Zipcode.py
************************** Testing Positive Scenarios **************************
Testing with input: ''. Expecting: '00000'. Obtained: '00000'
Testing with input: '1'. Expecting: '00001'. Obtained: '00001'
Testing with input: '1234'. Expecting: '01234'. Obtained: '01234'
Testing with input: '12345'. Expecting: '12345'. Obtained: '12345'
Testing with input: '1234567890'. Expecting: '1234567890'. Obtained: '1234567890'
Testing with input: '123456789'. Expecting: '12345-6789'. Obtained: '12345-6789'
********************************************************************************
.********************** Testing Unhandled Input Scenarios ***********************
Testing with input: '123456'. Expecting: 'None'. Obtained: 'None'
Testing with input: '12345678'. Expecting: 'None'. Obtained: 'None'
Testing with input: '12345678901'. Expecting: 'None'. Obtained: 'None'
********************************************************************************
.********************* Testing Special Char Input Scenarios *********************
Testing with input: '---------'. Expecting: '----------'. Obtained: '----------'
Testing with input: '@#$%'. Expecting: '0@#$%'. Obtained: '0@#$%'
********************************************************************************
.****************************** Testing Exceptions ******************************
Testing without providing the function argument
Testing with passing integer argument, instead of string
********************************************************************************
.
----------------------------------------------------------------------
Ran 4 tests in 0.003s

OK

C:\Backup\INSOFE\OneDrive\Accion_Rackspace\git_copy\Accion_SDET>
C:\Backup\INSOFE\OneDrive\Accion_Rackspace\git_copy\Accion_SDET>python Q2_Return_Unique.py
************************** Testing Positive Scenarios **************************
Testing with input: '('abcd', 'cdef')'. Expecting: 'abef'. Obtained: 'abef'
Testing with input: '('abcdxy', 'cdefst')'. Expecting: 'abxyefst'. Obtained: 'abxyefst'
Testing with input: '('12345', '4567890')'. Expecting: '12367890'. Obtained: '12367890'
Testing with input: '('aaabcdd', 'cdeeef')'. Expecting: 'aaabdeeef'. Obtained: 'aaabdeeef'
Testing with input: '('abcd', 'CDef')'. Expecting: 'abcdCDef'. Obtained: 'abcdCDef'
Testing with input: '('abcd', 'efgh')'. Expecting: 'abcdefgh'. Obtained: 'abcdefgh'
Testing with input: '('abcd', 'abcd')'. Expecting: ''. Obtained: ''
Testing with input: '('abcd', '')'. Expecting: 'abcd'. Obtained: 'abcd'
Testing with input: '('', 'efgh')'. Expecting: 'efgh'. Obtained: 'efgh'
Testing with input: '('', '')'. Expecting: ''. Obtained: ''
********************************************************************************
.****************************** Testing Exceptions ******************************
Testing without providing all or one function argument
Testing with passing integer argument, instead of string
********************************************************************************
.
----------------------------------------------------------------------
Ran 2 tests in 0.002s

OK

C:\Backup\INSOFE\OneDrive\Accion_Rackspace\git_copy\Accion_SDET>
C:\Backup\INSOFE\OneDrive\Accion_Rackspace\git_copy\Accion_SDET>python Q3_Multiple_Functions.py
************************ Testing check_integer_range() *************************
Testing with input: '4'. Expecting: 'True'. Obtained: 'True'
Testing with input: '10'. Expecting: 'True'. Obtained: 'True'
Testing with input: '8'. Expecting: 'True'. Obtained: 'True'
Testing with input: '3'. Expecting: 'False'. Obtained: 'False'
Testing with input: '11'. Expecting: 'False'. Obtained: 'False'
Testing with input: '9223372036854775807'. Expecting: 'False'. Obtained: 'False'
Testing with input: 'inf'. Expecting: 'False'. Obtained: 'False'
Testing with input: '-inf'. Expecting: 'False'. Obtained: 'False'
Testing with input: 'nan'. Expecting: 'False'. Obtained: 'False'
Testing with Non-Numeric argument
Testing without providing all or one function argument
********************************************************************************
.***************************** Testing check_list() *****************************
Testing with input: '[]'. Expecting: 'EMPTY'. Obtained: 'EMPTY'
Testing with input: '[1]'. Expecting: 'NOT EMPTY'. Obtained: 'NOT EMPTY'
Testing with input: '[1, 2, 3, 4]'. Expecting: 'NOT EMPTY'. Obtained: 'NOT EMPTY'
Testing with input: '['a', 'b', 'c', 'd']'. Expecting: 'NOT EMPTY'. Obtained: 'NOT EMPTY'
Testing with Non-List argument
Testing without providing all or one function argument
********************************************************************************
.*************************** Testing write_to_file() ****************************
Testing with file: 'sample.txt' and  string: 'Valid file at current folder and valid input string'
Testing with file: 'sample.txt' and  string: 'Overwrting an existing file. File was created in previous testcase'
Testing with file: 'sample_folder\sample.txt' and  string: 'Valid file at differnt folder and valid input string'
Testing with file: 'sample.txt' and  non-string input: 12345
Testing with file: 'non_existing_folder\sample.txt' and  non-string input: This will throw an exception: FileNotFoundError
Testing with file: 'hidden_file.txt' and  non-string input: This will throw an exception: PermissionError
Testing with file: 'readonly_file.txt' and  non-string input: This will throw an exception: PermissionError
********************************************************************************
.************************ Testing double_list_elements() ************************
Testing with input: '[]'. Expecting: '[]'. Obtained: '[]'
Testing with input: '[1]'. Expecting: '[2]'. Obtained: '[2]'
Testing with input: '[1, 2, 3, 4]'. Expecting: '[2, 4, 6, 8]'. Obtained: '[2, 4, 6, 8]'
Testing with input: '[-11, -22, -33, -44]'. Expecting: '[-22, -44, -66, -88]'. Obtained: '[-22, -44, -66, -88]'
Testing with input: '['a', 'b', 'c', 'd']'. Expecting: '['aa', 'bb', 'cc', 'dd']'. Obtained: '['aa', 'bb', 'cc', 'dd']'
Testing with input: '[1, 2, 'x', 'y']'. Expecting: '[2, 4, 'xx', 'yy']'. Obtained: '[2, 4, 'xx', 'yy']'
Testing with input: '[1, 2, [11, 22]]'. Expecting: '[2, 4, [11, 22, 11, 22]]'. Obtained: '[2, 4, [11, 22, 11, 22]]'
Testing with input: '[1, 2, (11, 22), 4]'. Expecting: '[2, 4, (11, 22, 11, 22), 8]'. Obtained: '[2, 4, (11, 22, 11, 22), 8]'
Testing with input: 'None'. Expecting: '[]'. Obtained: '[]'
Testing without input. Expecting: '[]'. Obtained: '[]'
Testing with Non-List argument
Testing with Nested list with dictionary
Testing with Nested list with set
********************************************************************************
.
----------------------------------------------------------------------
Ran 4 tests in 0.017s

OK

C:\Backup\INSOFE\OneDrive\Accion_Rackspace\git_copy\Accion_SDET>
C:\Backup\INSOFE\OneDrive\Accion_Rackspace\git_copy\Accion_SDET>python Q4_OO_Excercise.py
************************* Working with Temporary class *************************
Name of t1: "t1Last, t1First [T]"
Pay rate of t2: 110
Vacation days of t1: 0
Agency name of t2: HireTemp1
Number of temporary employees: 2
********************************************************************************
************************ Working with Contractor class *************************
Name of c1: "c1Last, c1First [C]"
Pay rate of c2: 550
Vacation days of c3: 0
Agency name of c1: HireContractor1
Number of contractors: 3
********************************************************************************
************************* Working with Employee class **************************
Name of e1: "e1Last, e1First"
Pay rate of e2: 1600
Vacation days of e3: 20
Number of employees: 5
********************************************************************************
********************** Working with Base Class WorkForce ***********************
Total number of workers: 10
********************************************************************************

C:\Backup\INSOFE\OneDrive\Accion_Rackspace\git_copy\Accion_SDET>

