"""Interface Segregation Principle

"Many client-specific interfaces are better than one general-purpose interface."

"Suum cuique".

"""


"""
Let's look at the bad interface.
"""


class IShape:
    def draw_square(self):
        raise NotImplementedError

    def draw_rectangle(self):
        raise NotImplementedError

    def draw_circle(self):
        raise NotImplementedError


class Circle(IShape):
    def draw_square(self):
        pass

    def draw_rectangle(self):
        pass

    def draw_circle(self):
        pass


class Square(IShape):
    def draw_square(self):
        pass

    def draw_rectangle(self):
        pass

    def draw_circle(self):
        pass


class Rectangle(IShape):
    def draw_square(self):
        pass

    def draw_rectangle(self):
        pass

    def draw_circle(self):
        pass


"""
The code above shows us many useless methods. So, let's change the approach
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


"""
Now the interfaces are simple.
"""