from new import check
a=int(input("enter a number="))
check(a)   

# FUNCTIONS
# A function is a reusable block of code that performs a specific task.
# Functions can be built-in (already provided by Python)
# or user-defined (created by the programmer).


# GLOBAL AND LOCAL VARIABLES
# A global variable is declared outside a function and can be accessed
# from different parts of the program.
#
# A local variable is declared inside a function and can normally be
# accessed only within that function.


# PASSING ARGUMENTS
# Arguments are the values passed to a function when it is called.
# Example: in add(x, y), x and y receive the values passed to the function.
#(Value passing)

# IMPORTING A FUNCTION
# A function written in another Python file can be imported and used
# in the current file.

#return
def add(s,t):
    return s+t
print(add(1,2))    
