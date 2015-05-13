class Laptop:
    device = "notebook"
    """
    >here u go for instance method which only access through object
    not by class name
    """

    def __init__(self):
        print "hi from laptop class"
        print self.device

    def get_device_name(self):
        return self.device

    def get_class_device(self):
        print 'Myself=>', self, self.__class__
        return self.__class__.device


class Laptop_class_method:
    device =  "mobile type"

    def __init__(self):
        self.device = "mini tab"


    def get_name(self):
        print self.device
    """
    >here u can see class method which can be access through object as well as class name
    but when accessing through object, value of device name will be different
    > class method, device variable value not depend on object when
      method will call through object it will give the value which was define in class level not instance
    > here cls will replace with object when it will call by object
        """
    @classmethod
    def get_class_device(cls, device):
        print "myself", cls
        cls.device = device
        return cls.device


class Laptop_static_method:

    brand_name = "Dell"
    popularity = 5

    def __init__(self):
        self.country = "India"
    """
    >here u go for static method either u can declare as before function or u can call with staticmethod(fun_name)
    """
    def get_name():
        return Laptop_static_method.brand_name

    def edit_rating(self, n):
        self.popularity = n

    @staticmethod
    def get_popularity():
        return Laptop_static_method.popularity

    get_name = staticmethod(get_name)

