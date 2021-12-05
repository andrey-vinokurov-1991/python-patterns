"""Open-Closed Principle.

"Software entities(Classes, modules, functions) should be open for extension, not modification."

When in Rome, do as the Romans do
 or build your own city based on Rome and build new habits.

Software entities(classes, modules, functions) should be open for extension,
 not modification.
"""
from abc import abstractmethod
from typing import List


class ElementBrokenOCP:
    def __init__(self, name: str):
        self._name = name

    @property
    def name(self) -> str:
        return self._name


def element_animal_broken_ocp(elements: List):
    for element in elements:
        if element.name == "Water":
            print("Snake")
        elif element.name == "Gold":
            print("Tiger")
    print("\n")


elements_example_broken_ocp = [
    ElementBrokenOCP("Water"),
    ElementBrokenOCP("Gold"),
    ElementBrokenOCP("Metal")
]

element_animal_broken_ocp(elements_example_broken_ocp)
"""
For the way described above
 we have to change our function every time when we add a new element.
That breaks Open-Closed Principle.
The way described below is correct.
"""


class Element:
    def __init__(self, name: str):
        self._name = name

    @property
    def name(self) -> str:
        return self._name

    @abstractmethod
    def get_animal(self) -> str:
        pass


class Water(Element):
    def __init__(self):
        super().__init__("Water")

    def get_animal(self) -> str:
        return "Snake"


class Gold(Element):
    def __init__(self):
        super().__init__("Gold")

    def get_animal(self) -> str:
        return "Tiger"


class Tree(Element):
    def __init__(self):
        super().__init__("Tree")

    def get_animal(self) -> str:
        return "Monkey"


def element_animal(elements: List[Element]):
    for element in elements:
        print(element.get_animal())


elements_example = [Water(), Gold(), Tree()]

element_animal(elements_example)
