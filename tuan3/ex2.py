class SieuNhan:
    def __init__(self, ten, vu_khi, mau_sac):
        self.ten = ten
        self.vu_khi = vu_khi
        self.mau_sac = mau_sac

    def show(self):
        print(f"Siêu nhân {self.ten} có {self.vu_khi} và màu sắc {self.mau_sac}")


sn1 = SieuNhan("Iron Man", "Giáp", "Đỏ")
sn2 = SieuNhan("Thor", "Búa", "Xám")

sn1.show()
sn2.show()
