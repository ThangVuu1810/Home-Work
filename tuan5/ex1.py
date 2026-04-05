class HangHoa:
    def __init__(self, ma_hang, ten_hang, gia):
        self.ma_hang = ma_hang
        self.ten_hang = ten_hang
        self.gia = gia

    def hien_thi(self):
        print(f"Mã: {self.ma_hang}, Tên: {self.ten_hang}, Giá: {self.gia}")

class HangDienMay(HangHoa):
    def __init__(self, ma_hang, ten_hang, gia, thoi_gian_bao_hanh, cong_suat):
        super().__init__(ma_hang, ten_hang, gia)
        self.thoi_gian_bao_hanh = thoi_gian_bao_hanh
        self.cong_suat = cong_suat

    def hien_thi(self):
        super().hien_thi()
        print(f"Bảo hành: {self.thoi_gian_bao_hanh}, Công suất: {self.cong_suat}")

class HangDamSu(HangHoa):
    def __init__(self, ma_hang, ten_hang, gia, nha_san_xuat, chat_lieu):
        super().__init__(ma_hang, ten_hang, gia)
        self.nha_san_xuat = nha_san_xuat
        self.chat_lieu = chat_lieu

    def hien_thi(self):
        super().hien_thi()
        print(f"NSX: {self.nha_san_xuat}, Chất liệu: {self.chat_lieu}")

class HangThucPham(HangHoa):
    def __init__(self, ma_hang, ten_hang, gia, ngay_sx, ngay_het_han):
        super().__init__(ma_hang, ten_hang, gia)
        self.ngay_sx = ngay_sx
        self.ngay_het_han = ngay_het_han

    def hien_thi(self):
        super().hien_thi()
        print(f"NSX: {self.ngay_sx}, HSD: {self.ngay_het_han}")

print("Thông tin hàng hóa:")

h1 = HangDienMay("DM01", "Tivi", 10000, "24 tháng", "100W")
h2 = HangDamSu("DS01", "Chén", 200, "Bát Tràng", "Sứ")
h3 = HangThucPham("TP01", "Sữa", 50, "01-01-2024", "01-06-2024")

h1.hien_thi()
h2.hien_thi()
h3.hien_thi()
