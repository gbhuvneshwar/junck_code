__str__ is used in to show a string representation of your object to be read easily by others.

__repr__ is used to show a string representation of the object.

Let's say I want to create a Fraction class where the string representation of a fraction is '(1/2)' and the object (Fraction class) is to be represented as 'Fraction (1,2)'

So we can create a simple Fraction class:

class Fraction:
    def __init__(self, num, den):
        self.__num = num
        self.__den = den

    def __str__(self):
        return '(' + str(self.__num) + '/' + str(self.__den) + ')'

    def __repr__(self):
        return 'Fraction (' + str(self.__num) + ',' + str(self.__den) + ')'



f = Fraction(1,2)
print('I want to represent the Fraction STRING as ' + str(f)) # (1/2)
print('I want to represent the Fraction OBJECT as ', repr(f)) # Fraction (1,2)

###################################

"A basic requirement for a Python object is to provide usable 
 string   representations of itself, one used for debugging and
 logging, another for presentation to end users. 
-->you implement should have a functional __repr__ that’s usable for understanding the object.
That is why the special methods __repr__ and __str__ exist in the data model."
