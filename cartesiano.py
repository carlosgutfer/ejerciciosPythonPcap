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


point1 = Point(0, 0)
point2 = Point(1, 1)
print(point1.distance_from_point(point2))
print(point2.distance_from_xy(2, 0))
