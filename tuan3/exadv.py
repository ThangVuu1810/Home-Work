
class NhanVien:
    LUONG_MAX = 50_000_000  # hằng số class

    def __init__(self, ten, luong_co_ban, he_so_luong):
        self.ten = ten
        self.luong_co_ban = luong_co_ban
        self.he_so_luong = he_so_luong

    def tinh_luong(self):
        return self.luong_co_ban * self.he_so_luong

    def in_tt(self):
        print(f"{self.ten} - Lương: {self.tinh_luong()}")

    def tang_luong(self, delta):
        if self.tinh_luong() + delta <= NhanVien.LUONG_MAX:
            self.luong_co_ban += delta / self.he_so_luong
