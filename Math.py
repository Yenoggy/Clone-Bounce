from math import sqrt
def Normalize(Vec):
    Magnitude = sqrt(Vec.x**2 +Vec.y**2)
    Vec.x = Vec.x/Magnitude
    Vec.y = Vec.y/Magnitude
    return Vec