from math import gcd

class MauSoBangKhong(Exception):
    pass

class PhanSo:
    def __init__(self, tu, mau):
        if mau == 0:
            raise MauSoBangKhong("Mẫu số không được bằng 0")
        self.__tu = tu
        self.__mau = mau

    @property
    def tu(self):
        return self.__tu

    @property
    def mau(self):
        return self.__mau

    def toi_gian(self):
        ucln = gcd(self.__tu, self.__mau)
        tu = self.__tu // ucln
        mau = self.__mau // ucln

        if mau < 0:
            tu = -tu
            mau = -mau

        return PhanSo(tu, mau)

    def is_toi_gian(self):
        return gcd(self.__tu, self.__mau) == 1

    def __add__(self, other):
        tu = self.__tu * other.mau + other.tu * self.__mau
        mau = self.__mau * other.mau
        return PhanSo(tu, mau).toi_gian()

    def __sub__(self, other):
        tu = self.__tu * other.mau - other.tu * self.__mau
        mau = self.__mau * other.mau
        return PhanSo(tu, mau).toi_gian()

    def __mul__(self, other):
        return PhanSo(self.__tu * other.tu, self.__mau * other.mau).toi_gian()

    def __truediv__(self, other):
        if other.tu == 0:
            raise ZeroDivisionError("Không thể chia cho phân số 0")
        return PhanSo(self.__tu * other.mau, self.__mau * other.tu).toi_gian()

    def __eq__(self, other):
        return self.__tu * other.mau == other.tu * self.__mau

    def __lt__(self, other):
        return self.__tu * other.mau < other.tu * self.__mau

    def __gt__(self, other):
        return self.__tu * other.mau > other.tu * self.__mau

    def __str__(self):
        ps = self.toi_gian()
        if ps.mau == 1:
            return f"{ps.tu}"
        return f"{ps.tu}/{ps.mau}"

    def __repr__(self):
        return f"PhanSo({self.__tu}, {self.__mau})"
    
ds = []

n = int(input("Nhập số lượng phân số: "))

for i in range(n):
    tu = int(input(f"Nhập tử số {i+1}: "))
    mau = int(input(f"Nhập mẫu số {i+1}: "))
    try:
        ps = PhanSo(tu, mau)
        ds.append(ps)
    except MauSoBangKhong as e:
        print("Lỗi:", e)

print("\n=== Phân số tối giản ===")
for ps in ds:
    print(ps)

ds_sorted = sorted(ds)

print("\n=== Sau khi sắp xếp tăng dần ===")
for ps in ds_sorted:
    print(ps)
