"""
Challenge 102 of project euler - Triangle Containment

@author Ori Dabush
"""

from utils.inputs import get_input
from dataclasses import dataclass


@dataclass
class Point:
    x: int
    y: int


class Line:
    def __init__(self, p1, p2):
        self.m = Line._slope(p1, p2)
        self.b = p1.y - self.m * p1.x
        self.p1 = p1
        self.p2 = p2

    def _slope(p1, p2):
        if p1.x == p2.x:
            return None
        return (p2.y - p1.y) / (p2.x - p1.x)

    def _calc(self, x):
        if self.m is None:
            return None
        return self.m * x + self.b

    def point_reference(self, p):
        y = self._calc(p.x)
        if p.y > y:
            # point is above the line
            return 1
        elif p.y == y:
            # point is on the line
            return 0
        elif p.y < y:
            # point is below the line
            return -1


def contains_origin(t):
    a,b,c = sorted(t, key=lambda p: p.x)
    if a.x > 0 or c.x < 0:
        return False
    l1 = Line(a, c)
    if b.x < 0:
        l2 = Line(b, c)
    else:
        l2 = Line(a, b)
    # l1 and l2 are the edges which possibly bounds the origin
    # Let's check if the origin is between them (i.e. below one and above the other)
    return {l1.point_reference(Point(0, 0)), l2.point_reference(Point(0, 0))} == {-1, 1}


def get_triangles():
    lines = get_input(102).strip().split()
    triangles = []
    for line in lines:
        values = list(map(int, line.split(',')))
        triangles.append(
            tuple(Point(*values[i:i+2]) for i in range(0, len(values), 2))
        )
    return triangles


def solve():
    return len([t for t in get_triangles() if contains_origin(t)])


def main():
    print(f'The answer is {solve()}')


if __name__ == '__main__':
    main()
