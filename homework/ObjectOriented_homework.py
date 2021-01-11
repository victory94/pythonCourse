class Line:

    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    # distance = square root((x1-x2)^2 + (y1-y2)^2)
    def distance(self):
        x1, y1 = self.coor1
        x2, y2 = self.coor2
        return ((x1 -x2)**2+(y1-y2)**2)**0.5

    # slope = y2-y1/x2-x1
    def slope(self):
        x1, y1 = self.coor1
        x2, y2 = self.coor2
        return (y2-y1)/(x2-x1)

    def __str__(self):
        return f"{self.distance}"


class Cylinder:
    pi = 3.14

    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius

    # V = π r ^2 * h
    def volume(self):
        return Cylinder.pi*(self.radius**2)*self.height

    # π r 2 * h + 2π r ^2
    def surface_area(self):
        top = Cylinder.pi*(self.radius**2)
        return (2*top)+(2*Cylinder.pi*self.radius*self.height)


if __name__ == '__main__':
    coordinate1 = (3, 2)
    coordinate2 = (8, 10)

    li = Line(coordinate1, coordinate2)
    print(li.distance())
    print(li.slope())

    c = Cylinder(2,3)
    print(str(c.volume()))
    print(c.surface_area())
