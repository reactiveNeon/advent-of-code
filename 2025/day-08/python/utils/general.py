import math


Point = tuple[int, int, int]

def distance(p1: Point, p2: Point):
    x1, y1, z1 = p1
    x2, y2, z2 = p2

    dx_sq = (x2 - x1) ** 2
    dy_sq = (y2 - y1) ** 2
    dz_sq = (z2 - z1) ** 2

    return math.sqrt(dx_sq + dy_sq + dz_sq)