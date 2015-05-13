class Parent(object):
    def __init__(self, name, age):
        print "hello from Parent"
        self._name = name
        self._age = age
        self._x = 10

    def __call__(self, *args):
        print "hi from call"
        self._name = args[0]
        return self._name

    """
        >when object of class is created that time name and age will get initilized
         with the value we pass.
        > call method is called from the reference variable of the object with argument and
         changed the value of the attribute for particular object
    """

    def get_name(self):
        return self._name


class Child(Parent):

    def __init__(self, name, age):
        print "hello from child"
        self._x = 15
        super(Child, self).__init__(name, age)

        print "parent attribute is initilizing"

    """
     > whenever object of child class is created, first it will call to
       parent class init method using super keyword and attribute  which will
       pass will get initlized by parent init method

     >  here _x variable will initilized with 15 but after it is calling to super
        so value will refelect whatever will have in parent class
     > conceptually super keyword should be the very first otherwise it throw error but not in case of python
            """


class Gchild:
    _x = 25


class Ggchild(Parent, Gchild):

    def __init__(self):
        print "hi from Ggchild"

    """
    >here it will not call parent init method
     if wann call dont inililzed init method here
     but that time u need to pass same parameter what was parent init method have
        """