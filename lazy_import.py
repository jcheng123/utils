import math


class LazyProperty:
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            value = self.func(instance)
            setattr(instance, self.func.__name__, value)
            return value


class Circle:
    def __init__(self, radius):
        self.radius = radius

    @LazyProperty
    def area(self):  # set area method as a instance's property.
        print("Computing area")
        return math.pi * self.radius ** 2

    @LazyProperty
    def perimeter(self):  # set perimeter method as a instance's property.
        print("Computing perimeter")
        return 2 * math.pi * self.radius


if __name__ == "__main__":
    c = Circle(4.0)
    print("c.property: {}".format(vars(c)))
    print("c.area: {}".format(c.area))
    print("c.perimeter: {}".format(c.perimeter))
    del c.area
    print("c.property: {}".format(vars(c)))

    # weak point
    # From a grammatical point of view, this is not a mistake.
    # However, the area of a circle should be depended on the radius.
    c.area = 25
