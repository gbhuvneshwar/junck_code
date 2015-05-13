#Example for getting base classe's behavior mixed
# in the derived class doing the mixing behavior
# using co-operative multiple inheritance by using "super" .

class Machine(object):
    """ Base class for machines """

    def __init__(self, model, purpose, cpu_freq, memory,
                 screen_size, weight, dimension):
        self._x=10
        print 'Machine created.'

    def get_name(self):
        return 'Machine'

class Computer(Machine):
    """ Base class for any computing machine """

    def __init__(self, model, purpose, cpu_freq, memory,
                 screen_size, weight, dimension):

        super(Computer, self).__init__(model, purpose, cpu_freq,
                                     memory, screen_size,
                                     weight, dimension)
        self.model = model
        self.purpose = purpose
        self.cpu_freq = cpu_freq
        self.memory = memory
        print 'Created computer.'

    def get_name(self):
        return 'Computer'

class Portable(Machine):
    """ Any portable device """

    def __init__(self, model, purpose, cpu_freq, memory,
                 screen_size, weight, dimension):

        super(Portable, self).__init__(model, purpose, cpu_freq,
                                     memory, screen_size,
                                     weight, dimension)
        self.screen_size = screen_size
        self.weight = weight
        self.dimension = dimension
        print 'Created Portable.'

    def get_name(self):
        return 'Portable'

class Laptop(Computer, Portable):

    device = 'laptop'

    def __init__(self, model, purpose, cpu_freq, memory, screen_size, weight, dimension):
        # This method is not necessary if you are not doing anything
        # apart from simply calling super as below. Python will create
        # it for you with the right signature.
        super(Laptop, self).__init__(model, purpose, cpu_freq,
                                     memory, screen_size,
                                     weight, dimension)
        # Do something else for Laptop specific purposes
        print 'Created laptop.'

    def get_device(self):
        return self.device

    def get_class_device(self):
        return self.__class__.device