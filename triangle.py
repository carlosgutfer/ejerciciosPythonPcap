import math

class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__point = [x, y]

    def getx(self):
        return self.__point[0]

    def gety(self):
        return self.__point[1]

    def distance_from_xy(self, x, y):
        return math.sqrt(pow(x - self.getx(), 2) + pow(y - self.gety(), 2))


    def distance_from_point(self, point):
        return math.sqrt(pow(point.getx() - self.__point[0], 2) + pow(point.gety() - self.__point[1], 2))


class Triangle:
    def __init__(self, vertice1, vertice2, vertice3):
        self.__point = [vertice1, vertice2, vertice3] 

    def perimeter(self):
        return self.__point[0].distance_from_point(self.__point[1]) + self.__point[1].distance_from_point(self.__point[2]) + self.__point[2].distance_from_point(self.__point[0]) 


triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(triangle.perimeter())
