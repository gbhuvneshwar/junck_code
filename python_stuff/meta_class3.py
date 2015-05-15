"""
However, metaclasses actually define the type of a class, not just a factory
for it, so you can do much more with them. You can, for instance, define normal
methods on the metaclass. These metaclass-methods are like classmethods, in
that they can be called on the class without an instance, but they are also not
like classmethods in that they cannot be called on an instance of the class.
type.__subclasses__() is an example of a method on the 'type' metaclass. You
can also define the normal 'magic' methods, like __add__, __iter__ and
__getattr__, to implement or change how the class behaves.

"""


def make_hook(f):
    """Decorator to turn 'foo' method into '__foo__'"""
    f.is_hook = 1
    return f


class Mytype(type):
    def __new__(cls, name, bases, attrs):

        if name.startswith('None'):
            return None
        newattrs = {}

        for attrname, attrvalue in attrs.items():
            if getattr(attrvalue, 'is_hook', 0):
                newattrs['__%s__' % attrname] = attrvalue
            else:
                newattrs[attrname] = attrvalue
        return super(Mytype, cls).__new__(cls, name, bases, newattrs)

    def __int__(self, name, bases, attrs):

        super(Mytype, self).__init__(name, bases, attrs)

        # classregistry.register(self, self.interfaces)
        print "would register class %s now" % self

    def __add__(self, other):
        class Autoclass:
            print "Hi from __add__"
        return Autoclass

    def unregister(self):
        # classregistry.unregister(self)
        print "Would unregister class %s now." % self


class MyObject:
    __metaclass__ = Mytype


class NoneSamle(MyObject):
    b1 = 10

#print type(NoneSamle), repr(NoneSamle)


class Example(MyObject):

    def __init__(self, value):
       self.value = value

    @make_hook
    def add(self, other):
        return self.__class__(self.value + other.value)



e1 = Example(11)
print e1 + e1


class Sibling(MyObject):
    pass