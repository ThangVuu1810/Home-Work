from abc import ABC, abstractmethod

class GiaKhongHopLe(Exception):
    def __init__(self, gia):
        self.gia = gia
        super().__init__(f"Giá {gia} không hợp lệ")

class HangHoa(ABC):
    def __init__(self, ma, ten, nsx, gia):
        self.__ma = ma
        self.__ten = ten
        self.__nsx = nsx
        self.gia = gia  # dùng setter

    @property
    def ma_hang(self):
        return self.__ma

    @property
    def ten_hang(self):
        return self.__ten

    @property
    def gia(self):
        return self.__gia

    @gia.setter
    def gia(self, v):
        if v < 0:
            raise GiaKhongHopLe(v)
        self.__gia = v

    @abstractmethod
    def loai_hang(self):
        pass

    def inTTin(self):
        return (f"[{self.loai_hang()}] {self.__ma}"
                f" | {self.__ten} | {self.__gia:,.0f}đ")

    def __str__(self):
        return self.inTTin()

    def __eq__(self, o):
        if not isinstance(o, HangHoa):
            return False
        return self.__ma == o.ma_hang

    def __lt__(self, o):
        return self.__gia < o.gia

    def __hash__(self):
        return hash(self.__ma)


class HangDienMay(HangHoa):
    def __init__(self, ma, ten, nsx, gia, bh, dap, cs):
        super().__init__(ma, ten, nsx, gia)
        self.__bh = bh
        self.__cs = cs
        self.__dap = dap

    def loai_hang(self):
        return "Điện máy"

    def inTTin(self):
        return (f"{super().inTTin()}"
                f" | {self.__bh}th"
                f" | {self.__dap}V"
                f" | {self.__cs}W")
ds = [
    HangDienMay("DM01", "Tủ lạnh", "LG", 12000000, 24, 220, 150),
    HangDienMay("DM02", "Máy giặt", "Samsung", 9000000, 12, 220, 200)
]

# sắp xếp
for sp in sorted(ds):
    print(sp)

# lưu file
with open("kho.txt", "w", encoding="utf-8") as f:
    for sp in ds:
        f.write(str(sp) + "\n")
