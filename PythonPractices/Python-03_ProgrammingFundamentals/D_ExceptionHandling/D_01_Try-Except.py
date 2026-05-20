''' EXCEPTION HANDLING
- make the program deal with input errors

TRY... EXCEPT STATEMENTS
- will attempt to execute the code first to try if it will result to an error
- if errors occure, the code under except will be executed

Example:

try:
    getfile = open("myfile","r")
    getfile.write("My file for exception handling.")
except IOError:
    print("Unable to open or read the data in the file")
except:
    print("Some other error occurred!")
else:
    print("The file was written successfully.")

** Usually we only need the except IOError statement which checks only the cases in the try statement.
** An IOError is the "Input/Output Error" which indicates that an I/O operation fails. It can occur
when the program is trying to read or write a file or simply when there's a network connections or other data streams
** if some other error occurs, we might need another "general" except statement but it's not clear which
** ELSE statement is used to confirm that there are no errors found
** FINALLY statement: used to close the file no matter the end result. It closes the try..except statement
'''

try:
    getfile = open("myfile","r")
    getfile.write("My file for exception handling.")
except IOError:
    print("Unable to open or read the data in the file")
except:
    print("Some other error occurred!")
else:
    print("The file was written successfully.")


''' IOError / OSError (Python3):
- FileNotFoundError :   file doesn't exists
- PermissionError:      file is read-only or requires admin privileges
- IsADirectoryError:    opened a directory as if it were a file

'''