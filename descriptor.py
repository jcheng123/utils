# In general, a descriptor is an object attribute
# with "binding behavior", one whose attribute access
# has been overridden by methods in the descriptor protocol.
#
# Those methods are __get__(), __set__(), and __delete__().
# If any of those methods are defined for an object,
# it is said to be a descriptor.
#
# Descriptor Protocol
# descriptor.__get__(self, obj, type=None) --> value
# descriptor.__set__(self, obj, value) --> None
# descriptor.__delete__(self, obj) --> None
#
# A descriptor is implemented as a standard new
# style class in python.
#
# obj: the object where the attribute was accessed.
# owners: the class where the descriptor was assigned as an attribute.
#
# If an instance’s dictionary has an entry with the same name as a data descriptor,
# the data descriptor takes precedence.
# If an instance’s dictionary has an entry with the same name as a non-data descriptor,
# the dictionary entry takes precedence.


class Integer:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise AttributeError("Expected an int")
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        del instance.__dict__[self.name]


class Point:
    x = Integer('x')  # descriptor property
    y = Integer('y')

    def __init__(self, x, y):
        self.x = x
        self.y = y

# Alternatively, it is more common for a descriptor
# to be invoked automatically upon attribute access.
# For example, obj.d looks up d in the dictionary of obj.
# if d defines the method __get__(), then d.__get__(obj)
# is invoked according to the precedence rules listed below.
# To find a.x,
# firstly a.__dict__['x'],
# secondly, type(a).__dict['x']
# then continuing through the base classes of type(a)

if __name__ == "__main__":
    test_times = 100
    for num in range(test_times):
        x = num
        y = num + 1
        p = Point(x, y)

        # p.x is equal to Point.x.__get__(p, Point)
        # Instance variable vs Class variable.
        x_class_variable = Point.__dict__['x']
        print("Point.x: {}, Point.__dict__['x'].__get__(None, Point): {}"
              .format(Point.x, x_class_variable.__get__(None, Point)))

        x_instance_variable = p.__dict__['x']
        print("p.x: {}, Point.x.__get__(p, Point): {}"
              .format(p.x, Point.x.__get__(p, Point)))

        # p.y = 5 is equal to Point.y.__set__(p, 5)
        p.y = 5
        print("p.y: {}".format(p.y))
        Point.y.__set__(p, 34)
        print("Point.y.__set__(p, 34): {}", p.y)






