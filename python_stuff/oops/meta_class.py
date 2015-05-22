""""
A metaclass is the class of a class. Like a class defines how an instance of the class behaves,
a metaclass defines how a class behaves. A class is an instance of a metaclass

To create your own metaclass in Python you really just want to subclass 'type'.

Python creates a new class (when it executes the 'class' statement) by calling the metaclass.
Combined with the normal __init__ and __new__ methods
                                                         """


class Demo(object):
    def __init__(self):
        self.data = data

    def getd(self):
        return self.data * 3


class MyMeta(type):
    def __new__(metaname, classname, baseclasses, attrs):
        print "new called with"
        print 'metaname', metaname
        print 'classname', classname
        print 'baseclasses', baseclasses
        print 'attr', attrs
        #attrs['getdata'] = Demo.__dict__['getd']
        attrs['getdata'] = Demo.getd
        return type.__new__(metaname, classname, baseclasses, attrs)

    def __init__(classobject, classname, baseclasses, attrs):
        print "init called with"
        print "classobject", classobject
        print "classname", classname
        print "baseclasses", baseclasses
        print "attrs", attrs


class A(object):
    __metaclass__ = MyMeta

    def __int__(self):
        self.data = data
        pass

    def printd(self):
        print self.data

a1 = A()
a1.printd()


