"""Liskov Substitution Principle.

Don't Forget Your Roots.

A sub-class must be substitutable for its super-class.  The aim of this
principle is to ascertain that a sub-class can assume the place of its
super-class without errors. If the code finds itself checking the type of class
then, it must have violated this principle.
"""


class VehicleBrokenLSP:
    """A demo Vehicle class."""
    def __init__(self, name: str):
        self.name = name

    def get_name(self) -> str:
        """Get vehicle name."""
        return f"The vehicle name {self.name}"

    def engine(self):
        """A vehicle engine."""
        print(f"The engine of {self.name} has been started")

    def start_engine(self):
        """A vehicle engine start."""
        self.engine()


class CarBrokenLSP(VehicleBrokenLSP):
    """A demo Car Vehicle class."""
    def start_engine(self):
        pass


class FlinstonesCarBrokenLSP(VehicleBrokenLSP):
    """A demo The Flinstones Car Vehicle class."""
    def start_engine(self):
        pass


"""
In the Flinstones car class violates the LSP.
Cause in the Vehicle class has an engine method.
But naturally, a the Flinstones car has no engine.
So we could not start any engine.
"""


class Vehicle:
    """A demo Vehicle class."""
    def __init__(self, name: str):
        self.name = name

    def get_name(self) -> str:
        """Get vehicle name."""
        return f"The vehicle name {self.name}"


class VehicleWithoutEngine(Vehicle):
    """A demo Vehicle without engine class."""
    def start_moving(self):
        """Moving."""
        raise NotImplementedError


class VehicleWithEngine(Vehicle):
    """A demo Vehicle engine class."""
    def engine(self):
        """A vehicle engine."""
        print(f"The engine of {self.name} has been started")

    def start_engine(self):
        """A vehicle engine start."""
        self.engine()


class Car(VehicleWithEngine):
    """A demo Car Vehicle class."""
    def start_engine(self):
        pass


class FlinstonesCar(VehicleWithoutEngine):
    """A demo The Flinstones Car Vehicle class."""
    def start_moving(self):
        pass
