class NhanVien:
    def __init__(self, ten, he_so_luong, luong_co_ban):
        self.__ten = ten
        self.__he_so_luong = he_so_luong
        self.__luong_co_ban = luong_co_ban

    # Getter
    def get_ten(self):
        return self.__ten

    def get_he_so_luong(self):
        return self.__he_so_luong

    def get_luong_co_ban(self):
        return self.__luong_co_ban

    # Setter
    def set_ten(self, ten):
        self.__ten = ten

    def set_he_so_luong(self, hsl):
        self.__he_so_luong = hsl

    def set_luong_co_ban(self, lcb):
        self.__luong_co_ban = lcb

    # Method
    def tinh_luong(self):
        return self.__he_so_luong * self.__luong_co_ban

    def tang_luong(self, tang):
        self.__he_so_luong += tang

    def in_tt(self):
        print("Ten:", self.__ten)
        print("He so luong:", self.__he_so_luong)
        print("Luong co ban:", self.__luong_co_ban)
        print("Luong:", self.tinh_luong())
