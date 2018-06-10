import math

class Point:

    def __init__(self,x,y):
        self.x=x
        self.y=y

    def getDistance(self):
        return math.sqrt(self.x^2+self.y^2)

    def getQuadrant(self):
        if self.x>0 and self.y>0:
            return ("I")
        elif self.x<0 and self.y>0:
            return ("II")
        elif self.x<0 and self.y<0:
            return ("III")
        else:
            return ("IV")

    def movePoint(self,deltax,deltay):
        self.x+=deltax
        self.y+=deltay

class Point3D:

    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z

    def getDistanceFromOrigin(self):
        return math.sqrt(self.x**2+self.y**2+self.z**2)

point1=Point(7,7)
print(point1.getQuadrant())
print(point1.getDistance())
point3D1=Point3D(2,6,9)
print(point3D1.getDistanceFromOrigin())
