
class MyInteger(object):
    """ Wrapper class on Python integers """

    def __init__(self, value=0):
        """ Initializer, accepts an integer """
        if type(value) is not int:
            raise TypeError, "I accept only integers"
        self._value = value

    def get_value(self):
        """ Return my value """
        return self._value

    def __int__(self):
        return self._value

    def __neg__(self):
        return -1*self._value
    
    def __str__(self):
        """ Return string representation of myself """
        return "(integer): " + str(self._value)
        
    def __eq__(self, other):
        """ Overloaded equality operator == """
        if type(other) is int:
            return self._value == other
        elif type(other) is MyInteger:
            return (self._value == other.get_value())

    def __ne__(self, other):
        """ Overloaded inequality operator != """
        return (self._value != other.get_value())     

    def __lt__(self, other):
        """ Overloaded < operator """
        return (self._value < other.get_value())

    def __gt__(self, other):
        """ Overloaded > operator """
        return (self._value > other.get_value())      

    def __le__(self, other):
        """ Overloaded <= operator """
        return (self._value <= other.get_value())     

    def __ge__(self, other):
        """ Overloaded >= operator """
        return (self._value >= other.get_value())     

    def __add__(self, other):
        """ Overloaded + operator """

        print 'Inside __add__'
        if type(other) is MyInteger:
            return self._value + other.get_value()          
        elif type(other) is int:
            return self._value + other

    def __iadd__(self, other):
        """ Overloaded += operator """

        if type(other) is MyInteger:
            self._value += other.get_value()          
        elif type(other) is int:
            self._value += other

        # Need to return a reference to self.
        return self
        
    def __radd__(self, other):
        """ Overloaded reverse + operator """

        print 'Inside __radd__'     
        if type(other) is MyInteger:
            return self._value + other.get_value()          
        elif type(other) is int:
            return self._value + other

    def __sub__(self, other):
        """ Overloaded - operator """
        if type(other) is MyInteger:
            return self._value - other.get_value()
        elif type(other) is int:
            return self._value - other

    # Gotcha here.
    def __rsub__(self, other):
        """ Overloaded reverse - operator """
        if type(other) is MyInteger:
            return other.get_value() - self._value 
        elif type(other) is int:
            return other - self._value 
    
    def __mul__(self, other):
        """ Overloaded * operator """
        return self._value * other.get_value()  

    def __div__(self, other):
        """ Overloaded / operator """
        return self._value / other.get_value()