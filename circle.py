from typing import TypeVar, Generic, Optional

T = TypeVar("T")


class DoubleLink(Generic[T]):
    def __init__(self, element: Optional[T] = None):
        self.element: Optional[T] = element
        self.next: Optional[DoubleLink[T]] = None
        self.prev: Optional[DoubleLink[T]] = None


class Circle:

    def remove_next(self) -> int:
        """
        Remove the next person (only one!) from the circle according to the rules.
        :return: The number (name) of the person removed.
        """
        pass

    def print_circle(self):
        """
        Prints the numbers (names) of the people currently in the circle.
        Starts from the current counting position and proceeds clockwise.
        Format is one-line, comma separated. Ex: `circle is now 4, 5, 1, 2`
        """
        pass
