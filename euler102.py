from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
Triangle = namedtuple('Triangle', ['A', 'B', 'C'])

def subsPoints(A: Point, B: Point) -> Point:
    return Point(A.x - B.x, A.y - B.y)

def Point_in_Triangle(P: Point, t: Triangle) -> bool:
    mB, mC, mO = subsPoints(t.B, t.A), subsPoints(t.C, t.A), subsPoints(origo, t.A)
    t = Triangle(t.A, mB, mC)
    P = mO
    d = (t.B.x * t.C.y) - (t.C.x * t.B.y)
    w_A = (P.x * (t.B.y - t.C.y) + P.y * (t.C.x - t.B.x) + (t.B.x * t.C.y) - (t.C.x * t.B.y)) / d
    w_B = ((P.x * t.C.y) - (P.y * t.C.x)) / d
    w_C = ((P.y * t.B.x) - (P.x * t.B.y)) / d
    return all([0 < w_A < 1, 0 < w_B < 1, 0 < w_C < 1])

origo = Point(0, 0)

triangle_coords = [list(map(int, line.strip().split(","))) for line in open('euler102_triangles.txt')]
points = [[Point(*l[:2]), Point(*l[2:4]), Point(*l[4:])] for l in triangle_coords]
triangles = [Triangle(*line) for line in points]

count = 0
for t in triangles:
    if Point_in_Triangle(origo, t):
        count += 1
# print(count)
