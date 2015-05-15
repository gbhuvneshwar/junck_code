"""
Now, let's do exactly the same, but using a real class for a metaclass:
remember that `type` is actually a class like `str` and `int`
so you can inherit from it
-------------------------------------------------------
    # __new__ is the method called before __init__
    # it's the method that creates the object and returns it
    # while __init__ just initializes the object passed as parameter
    # you rarely use __new__, except when you want to control how the object
    # is created.
    # here the created object is the class, and we want to customize it
    # so we override __new__
    # you can do some stuff in __init__ too if you wish
    # some advanced use involves overriding __call__ as well, but we won't
    # see this
---------------------------------------------------------------

    When type is called, its __call__ method is called.
    This method in turn calls the __new__ and __init__ methods


"""


class UpperAttrMetaclass(type):

        def __new__(refence, future_class, future_class_parent, future_class_attr):

            uppercase_attr = {}

            print "Hi from __new__"

            for name, val in future_class_attr.items():
                if not name.startswith('__'):
                    uppercase_attr[name.upper()] = val
                else:
                    uppercase_attr[name] = val
            return type.__new__(refence, future_class, future_class_parent, uppercase_attr)

        def __init__(refence, future_class, future_class_parent, uppercase_attr):
            print "Hi from inint"


class Foo():
    __metaclass__ = UpperAttrMetaclass
    s1 = 'hello'

    def __init__(self, data):
        print "hi from foo init"




f1 = Foo(12)
print f1.S1


"""
#op
Hi from __new__
Hi from inint
hi from foo init
hello
"""