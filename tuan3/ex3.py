class SieuNhan:
    def __init__(self, ten, vu_khi, mau_sac):
        self.ten = ten
        self.vu_khi = vu_khi
        self.mau_sac = mau_sac

    def show(self):
        print(f"Siêu nhân {self.ten} có {self.vu_khi} và màu sắc {self.mau_sac}")


ds = []

while True:
    ten = input("Nhập tên (Enter để dừng): ")
    if ten == "":
        break

    vu_khi = input("Nhập vũ khí: ")
    mau_sac = input("Nhập màu sắc: ")

    ds.append(SieuNhan(ten, vu_khi, mau_sac))


for sn in ds:
    sn.show()
