import math
class Circle:
    def __init__(self,centre,radius):
        self.centre = centre
        self.radius = radius


    def __contains__(self, point):
        distance =  (a-b for a,b in zip(self.centre,point))
        distance_from_radius = 0
        for i in distance:
            distance_from_radius += i**2
        distance_from_radius = math.sqrt(distance_from_radius)
        if distance_from_radius < self.radius:
            return True
        else:
            return False

