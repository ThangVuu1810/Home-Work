import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to(self, p):
        return math.sqrt((self.x - p.x)**2 + (self.y - p.y)**2)


class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def point_in_circle(self, p):
        return self.center.distance_to(p) <= self.radius

    def rect_in_circle(self, rect_points):
        return all(self.point_in_circle(p) for p in rect_points)

    def rect_circle_overlap(self, rect_points):
        return any(self.point_in_circle(p) for p in rect_points)
