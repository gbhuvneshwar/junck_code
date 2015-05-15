"""meta class:-->
Python will look for __metaclass__ in the class definition. If it finds it, it
will use it to create the object class Foo. If it doesn't, it will use type to
create the class.

Imagine a stupid example, where you decide that all classes in your module
should have their attributes written in uppercase. There are several ways to do
this, but one way is to set __metaclass__ at the module level.

This way, all classes of this module will be created using this metaclass, and
we just have to tell the metaclass to turn all attributes to uppercase.


"""

#tips-->>


def upper_attr(future_class, future_class_parent, future_class_attr):

    uppercase_attr = {}

    for name, val in future_class_attr.items():
        if not name.startswith('__'):
            uppercase_attr[name.upper()] = val
        else:
            uppercase_attr[name] = val

    return type(future_class, future_class_parent, uppercase_attr)


__metaclass__ = upper_attr
"""
Luckily, __metaclass__ can actually be any callable, it doesn't need to be a
formal class (I know, something with 'class' in its name doesn't need to be a
              class, go figure... but it's helpful).
"""

class Foo():
    bar = 'bip'


""""
global __metaclass__ won't work with "object" though
  ex, class Foo(object)
"""

print(hasattr(Foo, 'bar'))
#op False

print(hasattr(Foo, 'BAR'))
#op True

f1 = Foo()
print f1.BAR
#op bip


"""
This way, all classes of this module will be created using this metaclass, and
we just have to tell the metaclass to turn all attributes to uppercase.
"""

class F1():
    b1 = "hello"

print(hasattr(F1, 'B1'))

#op True

"""
now we have __metaclass__ in our module,it will create class according to our choice.
See in this module every class attribute  name is having uppercase.
if we declare class(object) it wont work

"""