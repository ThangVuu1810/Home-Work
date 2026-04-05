class CanBo:
    def __init__(self, ten):
        self.ten = ten

    def hien_thi(self):
        print(f"Tên: {self.ten}")

class CongNhan(CanBo):
    def __init__(self, ten, bac):
        super().__init__(ten)
        self.bac = bac

    def hien_thi(self):
        super().hien_thi()
        print(f"Bậc: {self.bac}")

class KySu(CanBo):
    def __init__(self, ten, nganh):
        super().__init__(ten)
        self.nganh = nganh

    def hien_thi(self):
        super().hien_thi()
        print(f"Ngành đào tạo: {self.nganh}")

class NhanVien(CanBo):
    def __init__(self, ten, cong_viec):
        super().__init__(ten)
        self.cong_viec = cong_viec

    def hien_thi(self):
        super().hien_thi()
        print(f"Công việc: {self.cong_viec}")

class QLCB:
    def __init__(self):
        self.danh_sach = []

    def them(self, canbo):
        self.danh_sach.append(canbo)

    def hien_thi(self):
        for cb in self.danh_sach:
            cb.hien_thi()
            print("-----")

    def tim_kiem(self, ten):
        for cb in self.danh_sach:
            if cb.ten == ten:
                cb.hien_thi()

ql = QLCB()

ql.them(CongNhan("Nam", 5))
ql.them(KySu("Lan", "CNTT"))
ql.them(NhanVien("Minh", "Kế toán"))

print("Danh sách:")
ql.hien_thi()

print("Tìm kiếm:")
ql.tim_kiem("Lan")
