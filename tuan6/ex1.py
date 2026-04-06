from abc import ABC, abstractmethod

class InvalidDataError(Exception):
    pass

class HangHoa(ABC):
    def __init__(self, ma_hang, ten_hang, gia_hang):
        self.ma_hang = ma_hang
        self.ten_hang = ten_hang
        self._gia_hang = gia_hang

    @property
    def gia_hang(self):
        return self._gia_hang

    @gia_hang.setter
    def gia_hang(self, value):
        if value < 0:
            raise InvalidDataError("Gia khong hop le")
        self._gia_hang = value

    @abstractmethod
    def tinh_thue(self):
        pass

    def __str__(self):
        return f"{self.ma_hang} | {self.ten_hang} | {self.gia_hang}"

    def __eq__(self, other):
        return self.ma_hang == other.ma_hang

    def __lt__(self, other):
        return self.gia_hang < other.gia_hang

class HangDienMay(HangHoa):
    def __init__(self, ma_hang, ten_hang, gia_hang, thoi_gian_bh, dien_ap, cong_suat):
        super().__init__(ma_hang, ten_hang, gia_hang)
        self.thoi_gian_bh = thoi_gian_bh
        self.dien_ap = dien_ap
        self.cong_suat = cong_suat

    def tinh_thue(self):
        return self.gia_hang * 0.1

    def __str__(self):
        return super().__str__() + f" | BH: {self.thoi_gian_bh} | {self.dien_ap}V | {self.cong_suat}W"

class HangSanhSu(HangHoa):
    def __init__(self, ma_hang, ten_hang, gia_hang, loai_nguyen_lieu):
        super().__init__(ma_hang, ten_hang, gia_hang)
        self.loai_nguyen_lieu = loai_nguyen_lieu

    def tinh_thue(self):
        return self.gia_hang * 0.05

    def __str__(self):
        return super().__str__() + f" | Chat lieu: {self.loai_nguyen_lieu}"

class HangThucPham(HangHoa):
    def __init__(self, ma_hang, ten_hang, gia_hang, ngay_sx, ngay_hh):
        super().__init__(ma_hang, ten_hang, gia_hang)
        self.ngay_sx = ngay_sx
        self.ngay_hh = ngay_hh

    def tinh_thue(self):
        return self.gia_hang * 0.02

    def __str__(self):
        return super().__str__() + f" | NSX: {self.ngay_sx} | NHH: {self.ngay_hh}"

class QuanLyKho:
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print(f"Error: {exc_val}")
        return True

if __name__ == "__main__":
    with QuanLyKho():
        h1 = HangDienMay("DM01", "Tu lanh", 5000, 24, 220, 150)
        h2 = HangSanhSu("SS01", "Bat trang", 100, "Gom")
        h3 = HangThucPham("TP01", "Sua", 20, "01/01/2024", "01/02/2024")
        
        print(h1)
        print(h2)
        print(h3)
