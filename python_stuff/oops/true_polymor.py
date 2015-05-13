 #True Polymorphism - Python does not give you overloaded methods
class Test1:
    name = "initial_test1"

    def __init__(self):
        self.name = "instnce_test1"

    @staticmethod
    def static_test():
        return Test1.name

    def bhuvi_test(self):
        return self.name

class Test2(Test1):
    name = "Test2_initial"

    def __init__(self):
        self.name = "instence_test2"

    def bhuvi_test(self, test):
        return test + self.name

    """
    > python does not follow true polymorphism
      here is two method with same name bhuvi_test with different argument
      but it will execute last method which is defined
    """

    def bhuvi_test(self):
        return self.name
