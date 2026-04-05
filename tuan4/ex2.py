class Point:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def clone(self):
        return Point(self.__x, self.__y)

    def in_tt(self):
        print(f"({self.__x}, {self.__y})")


class LineSegment:
    def __init__(self, d1=None, d2=None):
        if d1 is None:
            d1 = Point()
        if d2 is None:
            d2 = Point()

        self.__d1 = d1.clone()
        self.__d2 = d2.clone()

    def in_tt(self):
        print("Điểm 1:")
        self.__d1.in_tt()

        print("Điểm 2:")
        self.__d2.in_tt()
