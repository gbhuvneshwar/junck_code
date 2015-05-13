#Any error which happens during the execution of the code is an exception

#BaseException : BaseException is super class of SystemExit, KeyboardInterrupt, GeneratorExit, and Exception class.

#Exception: Exception is super class of StopIteration, StandardError,and Warning class

#StandardError:
> BufferError
> ArithmeticError (FloatingPointError,OverflowError,ZeroDivisionError)
> AssertionError
> AttributeError
>EnvironmentError (IOError,OSError)
>EOFError
>ImportError
>LookupError(IndexError,KeyError)
>MemoryError
>NameError(UnboundLocalError)
>ReferenceError
>RuntimeError(NotImplementedError)
>SyntaxError(IndentationError)
>SystemError
>TypeError
>ValueError

Assertion: Programmers often place assertions at the start of a function to check
           for valid input, and after a function call to check for valid output
           if not then raise AssertionError

"""
BaseException
 +-- SystemExit #Raised by the sys.exit() function
 +-- KeyboardInterrupt ##Raised when the user interrupts program execution,usually by pressing Ctrl+c.
 +-- GeneratorExit
 +-- Exception
      +-- StopIteration ## raise when next() method of an iterator does not point to any object.
      +-- StandardError ## Base class for following built-in exceptions
      |    +-- BufferError
      |    +-- ArithmeticError ## Base class for all errors that occur for numeric calculation.

      |    |    +-- FloatingPointError ##Raised when a floating point calculation fails.
      |    |    +-- OverflowError ##Raised when a calculation exceeds maximum limit for a numeric type.
      |    |    +-- ZeroDivisionError ##Raised when division or modulo by zero takes place for all numeric types.

      |    +-- AssertionError ##Raised in case of failure of the Assert statement.

      |    +-- AttributeError ##Raised in case of failure of attribute reference or assignment.
                               There will be no attribute defined for instance

      |    +-- EnvironmentError ##Base class for all exceptions that occur outside the Python environment.
      |    |    +-- IOError ## Raised when an input/ output operation fails,
                              such as the print statement or the open() function
                              when trying to open a file that does not exist.


      |    |    +-- OSError ##Raised for operating system-related errors.
      |    |         +-- WindowsError (Windows)
      |    |         +-- VMSError (VMS)

      |    +-- EOFError## Raised when there is no input from either the raw_input() or input() function
                          and the end of file is reached.
      |    +-- ImportError ##Raised when an import statement fails.

      |    +-- LookupError ##Base class for all lookup errors.
      |    |    +-- IndexError ## Raised when an index is not found in a sequence.

      |    |    +-- KeyError ## Raised when the specified key is not found in the dictionary.

      |    +-- MemoryError
      |    +-- NameError ## tries to a access variable which is not defined. Ex: print abc
                             it will give name error abc not defined.
                             Raised when an identifier is not found in the local or global namespace.
      |    |    +-- UnboundLocalError ##Raised when trying to access a local variable in a function or method
                                       but no value has been assigned to it.



      |    +-- ReferenceError
      |    +-- RuntimeError ## Raised when a generated error does not fall into any category.
      |    |    +-- NotImplementedError ##Raised when an abstract method that
                                          needs to be implemented in an inherited class is not actually implemented.
      |    +-- SyntaxError ## incorrect syntax ex: while true print "HI"
                               Here After true need (:)
                            #Raised when there is an error in Python syntax.
      |    |    +-- IndentationError
      |    |         +-- TabError
      |    +-- SystemError ## Raised when the interpreter finds an internal problem,
                             but when this error is encountered the Python interpreter does not exit.

      |    +-- TypeError ## tries to do an operation with different
                            kinds of incompatible data types.
                            A common example is to do addition of Integers and a string.

      |    +-- ValueError  ## Raised when the built-in function for a data type has the valid type of arguments,
                              but the arguments have invalid values specified.
                              Example-->
                                        def temp(var):
                                             return int(var)
                                        #if in argument we pass sting then value error will raised
                                        it was expecting no. got string

      |         +-- UnicodeError
      |              +-- UnicodeDecodeError
      |              +-- UnicodeEncodeError
      |              +-- UnicodeTranslateError
      +-- Warning
           +-- DeprecationWarning
           +-- PendingDeprecationWarning
           +-- RuntimeWarning
           +-- SyntaxWarning
           +-- UserWarning
           +-- FutureWarning
           +-- ImportWarning
           +-- UnicodeWarning
           +-- BytesWarning


"""


User-Defined Exception:-
    Python allow to create your own excpetion by deriving classes
    from standard build-in exceptions


class NetworkError(RuntimeError): #Here creating user define subclass from RuntimeError class

     def __init__(self. args):
          self.args = args

now raising exception:-

try:
     raise NetworkError("Bad HostName")
except NetworkError,e:
     print e.args


