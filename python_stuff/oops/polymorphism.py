 #True Polymorphism - Python does not give you overloaded methods
#like C++ with varying arguments.

class Laptop(Computer, Portable):

    def get_name(self, prefix):
        return prefix + '_laptop'

    def get_name(self):
        return 'Laptop'

#In this case the last implementation is chosen (silently). No exceptions.
