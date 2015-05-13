"""
Rules of thumb

1. Normal usage - Attributes accessed via instances.
Do nothing.
2. Class static data - Attributes that need to remain same
across all instances. Use classmethod with class level
attributes.
3. Class namespace used for functions - Functions that live
inside classes disguised as methods. Use staticmethod with
class level attributes (NOT ENCOURAGED!)
class Laptop(object):
    """ A laptop class """
    device = 'laptop'

    def __init__(self):
        self.device = 'notebook'

    def get_device(self):
        # Instance method - cannot be called directly on the class
        # gets a TypeError if you try to do that.
        return self.device

    def get_class_device(self):
        print 'Myself=>',self, self.__class__
        return self.__class__.device
"""

class Laptop2(object):
    """ A laptop class # 2 """

    # Can be accessed via the class directly
    # or via a classmethod.
    device = 'laptop'

    def __init__(self):
        self.device = 'notebook'

    def get_device(self):
        # Can be called directly on the class without
        # an instance. Can be called on the instance also
        # but will return the classe's attribute.

        print 'Myself=>',self
        return self.device

    @classmethod
    def set_device(self, device):
        # Every reference to self is replaced
        # with self.__class__
        print 'Myself=>',self
        self.device = device

    # More pythonic way of writing accessors
    # or setters for manipulating class attributes
    # via the instance.
    get_device = classmethod(get_device)
    # Try using a property on top of get_device and set_device
    # methods.

def get_brandname():
    return ComputerMaker.brand_name

class ComputerMaker(object):
    """ A class for computer makers """

    # Demoing static methods - try to use classmethods and
    # class static (class level) attributes instead of static
    # methods.

    brand_name = 'Toshiba'
    # Rating from 1-5
    popularity = 5

    def __init__(self):
        self.country = 'Japan'

    def get_brandname():
        # Remains unchanged across instances
        return ComputerMaker.brand_name

    @staticmethod
    def get_popularity():
        # Remains unchanged across instances
        return ComputerMaker.popularity

    def change_rating(self, rating):
        # Instance method - modified's the instance's
        # copy of 'popularity' attribute.
        self.popularity = rating

    # A function that lives inside a classe's namespace
    # completely unaware of any of the classes attributes.
    get_brandname = staticmethod(get_brandname)