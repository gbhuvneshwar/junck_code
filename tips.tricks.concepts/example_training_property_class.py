# Example code for properties in classes.

class Laptop(object):
    """ A basic laptop class with property proxies
    for attributes. """
    
    # Declare all data attributes for the class here
    
    def __init__(self):
        # Declare all data attribues here for the instance
        self.__device_name = 'laptop'
        self.__manufacturer = 'Toshiba'

    def __str__(self):
        return 'I am a ' + self.__manufacturer + ' ' + self.__device_name
    
    def display(self):
        print 'Laptop model=>',self.__manufacturer
        
    def get_device_name(self):
        print 'Getting device name'
        # Accessors or getters
        # BAD CODE! - should not modify what they access
        # self.device_name += '_someprefix'
        return self.__device_name

    def get_manufacturer(self):
        return self.__manufacturer

    def set_device_name(self, name):
        print 'Setting device name'
        # Setters should modify the attribute by
        # accepting params

        # Not advised to create dynamic attributes inside
        # functions - BAD CODE!
        # self.x=10
        self.__device_name = name

    def set_manufacturer(self, company):
        # Setters should modify the attribute by
        # accepting params
        self.__manufacturer = company

    def del_device_name(self):
        # Goes out of scope - Dangerous!
        del self.__device_name

    def del_pdisplay(self):
        del self.display
        
    # Properties are attribute proxies that stand for
    # an actual attribute and provides get/set on it via
    # fset/fget methods.
    dname=property(fget=get_device_name, fset=set_device_name)
    company=property(fget=get_manufacturer, fset=set_manufacturer)
    description=property(fget=__str__)