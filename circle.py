from typing import TypeVar, Generic, Optional

T = TypeVar("T")


class DoubleLink(Generic[T]):
    def __init__(self, element: Optional[T] = None):
        self.element: Optional[T] = element
        self.next: Optional[DoubleLink[T]] = None
        self.prev: Optional[DoubleLink[T]] = None


class Circle:
    def __init__(self):
        self.current: Optional[DoubleLink] = None
        self.size = 0

    def append(self, element: T):
        new_link = DoubleLink(element)
        if not self.current:
            self.current = new_link
            new_link.next = new_link
            new_link.prev = new_link
        else:
            tail = self.current.prev
            tail.next = new_link
            new_link.prev = tail
            new_link.next = self.current
            self.current.prev = new_link
        self.size += 1

    def remove_next(self) -> int:
        if not self.current or self.size == 0:
            return None
        to_remove = self.current.next
        if self.size == 1:
            removed_element = self.current.element
            self.current = None
        else:
            removed_element = to_remove.element
            self.current.next = to_remove.next
            to_remove.next.prev = self.current
        self.size -= 1
        return removed_element

    def print_circle(self):
        elements = []
        if self.current:
            start = self.current
            elements.append(start.element)
            node = start.next
            while node != start:
                elements.append(node.element)
                node = node.next
        print("circle is now " + ", ".join(map(str, elements)))

    def move_current(self, steps, clockwise=True):
        if not self.current:
            return
        step_range = range(abs(steps))
        for _ in step_range:
            if clockwise:
                self.current = self.current.next
            else:
                self.current = self.current.prev

