"""
                                     class Method
Now what if the method we want to write interacts with classes only
and not instances? We can code a simple function out of the class to do so
but that will spread the code related to class, to out of the class.
This can cause a future code maintenance problem, as follows:

"""


def test(cls_obj):
    return cls_obj.no_of_times


class A(object):

    no_of_times = 0

    def __init__(self):
        A.no_of_times = A.no_of_times + 1

#a1 = A()
#a2 = A()
#print test(a1)  #or print test(A)
#print test(A())

"""
test(A) it will just access the variable
but when we call test(A()) will call constructer

"""

#op = 2


"""
For avoiding confusion for future maintence
we can write declare above function as @classmethod
"""


class A(object):

    no_of_times = 0

    def __init__(self):
        A.no_of_times = A.no_of_times + 1

    @classmethod
    def test(cls):
        return cls.no_of_times

#a3 = A()
#print a3.test()

#OP = 1

#--------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------

"""
static method

Often there is some functionality that relates to the class,
but does not need the class or any instance(s) to do some work.
Perhaps something like setting environmental variables,changing an attribute in another class, etc.
In these situation we can also use a function,
however doing so also spreads the interrelated code which can cause maintenance issues later.

"""

name = "shivam"


def check():
    return name == "shivam"


class B(object):

    def __init__(self, data):
        self.data = data

    def do_set(self):
        if check():
            print self.data

    def do_call(self):
        if check():
            print self.data



#b1 = B(12)

#print b1.do_set()
#print b1.do_call()
#op--->>>>
#12
#None
#12
#None
""" basically in python static method is useless"""


class B(object):

    def __init__(self,data):
        self.data = data

    @staticmethod
    def check():
        return name == "shivam"

    def do_call(self):
        if self.check():
            print self.data

    def do_set(self):
        if self.check():
            print self.data


#b1 = B("Hello")
#b1.do_call()
#b1.do_set()
#op
#"hello"
#"hello"


"""..........................................................................................
     differnce b/w static and class method in python"""


class C(object):

    def __init__(self, data):
        self.data = data

    def pprint(self):
        print (self.data)

    @staticmethod
    def sprint(*args):
        print ("static:", args)

    @classmethod
    def cmethod(*a):
        print ("class:", a)
        print dir(a)


#c1 = C("hi")
#c1.pprint()
#c1.sprint()
#c1.cmethod()
#op
#hi
#('static:', ())
#('class:', (<class '__main__.C'>,))

#if call C.pprint() will give u "TypeError: unbound method printd() must be called with Kls instance as first argument (got nothing instead)"
#C.sprint() = ('static:', ())
#C.cmethod() = ('class:', (<class '__main__.C'>,))