'''
Exceptions are alerts when something unexpected happens when running a program

ERRORS VS EXCEPTIONS

ORIGIN
- ERRORS    :   typically caused by environment, hardware or OS
- EXCEPTIONS:   usually a result of problematic code execution

NATURE
- ERRORS    :   often severe and can lead to program crashes or abnormal termination
- EXCEPTIONS:   less severe and can be caught and handled to prevent termination

HANDLING
- ERRORS    :   not usually caught nor handled by program itself
- EXCEPTIONS:   can be caught with try-except blocks and dealth with gracefully, allowing
                the program to continue execution

EXAMPLES
- ERRORS    :   include "SyntaxError" due to incorrect syntax
                "NameError" when variable is not defined
- EXCEPTIONS:   "ZeroDivisionError" when dividing by 0
                "FileNotFuondError" when attempting to open a non-existing file

CATEGORIZATION
- ERRORS    :   not categorized
- EXCEPTIONS:   categorized into various classes:
                - "ArithmeticError"
                - "IOError"
                - "ValueError"
                - etc....

'''
