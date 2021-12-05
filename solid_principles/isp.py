"""Interface Segregation Principle

"Many client-specific interfaces are better than one general-purpose interface."

"Suum cuique".

"""


class IShape:
    def draw(self):
        raise NotImplementedError


class Circle(IShape):
    def draw(self):
        pass


class Square(IShape):
    def draw(self):
        pass


class Rectangle(IShape):
    def draw(self):
        pass
