class NhanVien:
    def __init__(self, ten, luong):
        self.ten = ten
        self.luong = luong

    def hien_thi(self):
        print(f"Tên: {self.ten}, Lương: {self.luong}")

class CongTacVien(NhanVien):
    def __init__(self, ten, luong, thoi_han_hd, phu_cap):
        super().__init__(ten, luong)
        self.thoi_han_hd = thoi_han_hd
        self.phu_cap = phu_cap

    def hien_thi(self):
        super().hien_thi()
        print(f"Thời hạn HĐ: {self.thoi_han_hd}, Phụ cấp: {self.phu_cap}")

class NhanVienChinhThuc(NhanVien):
    def __init__(self, ten, luong, vi_tri):
        super().__init__(ten, luong)
        self.vi_tri = vi_tri

    def hien_thi(self):
        super().hien_thi()
        print(f"Vị trí: {self.vi_tri}")

class TruongPhong(NhanVien):
    def __init__(self, ten, luong, ngay_bat_dau, phu_cap):
        super().__init__(ten, luong)
        self.ngay_bat_dau = ngay_bat_dau
        self.phu_cap = phu_cap

    def hien_thi(self):
        super().hien_thi()
        print(f"Ngày bắt đầu: {self.ngay_bat_dau}, Phụ cấp: {self.phu_cap}")


# Test
print("Thông tin nhân viên:")
nv1 = CongTacVien("A", 5000, "6 tháng", 500)
nv2 = NhanVienChinhThuc("B", 10000, "Developer")
nv3 = TruongPhong("C", 15000, "01-01-2023", 2000)

nv1.hien_thi()
nv2.hien_thi()
nv3.hien_thi()
