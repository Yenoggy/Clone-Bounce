from math import sqrt
def Normalize(Vec):
    if Vec.x == 0 and Vec.y == 0:
        Vec.y = 1
    Magnitude = sqrt(Vec.x**2 +Vec.y**2)
    Vec.x = Vec.x/Magnitude
    Vec.y = Vec.y/Magnitude
    return Vec