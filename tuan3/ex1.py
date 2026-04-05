import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"({self.x}, {self.y})")

    def distance_to(self, p):
        return math.sqrt((self.x - p.x) ** 2 + (self.y - p.y) ** 2)


# Tạo điểm A
A = Point(3, 4)
A.show()

# Nhập điểm B
x = float(input("Nhập x của B: "))
y = float(input("Nhập y của B: "))
B = Point(x, y)

# Điểm C đối xứng qua gốc O
C = Point(-B.x, -B.y)

# Gốc tọa độ
O = Point(0, 0)

print("B-O:", B.distance_to(O))
print("A-B:", A.distance_to(B))
