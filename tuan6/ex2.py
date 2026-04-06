from abc import ABC, abstractmethod

class TuoiKhongHopLe(Exception):
    pass

class BacKhongHopLe(Exception):
    pass

class CanBo(ABC):
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi):
        self.ho_ten = ho_ten
        self._tuoi = tuoi
        self.gioi_tinh = gioi_tinh
        self.dia_chi = dia_chi

    @property
    def tuoi(self):
        return self._tuoi

    @tuoi.setter
    def tuoi(self, value):
        if not (18 <= value <= 65):
            raise TuoiKhongHopLe("Tuoi phai tu 18 den 65")
        self._tuoi = value

    @abstractmethod
    def mo_ta(self):
        pass

    def __str__(self):
        return f"{self.ho_ten} | {self.tuoi} | {self.gioi_tinh} | {self.dia_chi}"

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.ho_ten == other.ho_ten and self.tuoi == other.tuoi

    def __lt__(self, other):
        return self.ho_ten.split()[-1] < other.ho_ten.split()[-1]

class CongNhan(CanBo):
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi, bac):
        super().__init__(ho_ten, tuoi, gioi_tinh, dia_chi)
        self._bac = bac

    @property
    def bac(self):
        return self._bac

    @bac.setter
    def bac(self, value):
        if not (1 <= value <= 10):
            raise BacKhongHopLe("Bac cong nhan phai tu 1 den 10")
        self._bac = value

    def mo_ta(self):
        return f"Cong nhan bac {self.bac}"

    def __str__(self):
        return super().__str__() + f" | {self.mo_ta()}"

class KySu(CanBo):
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi, nganh_dt):
        super().__init__(ho_ten, tuoi, gioi_tinh, dia_chi)
        self.nganh_dt = nganh_dt

    def mo_ta(self):
        return f"Ky su nganh {self.nganh_dt}"

    def __str__(self):
        return super().__str__() + f" | {self.mo_ta()}"

class NhanVien(CanBo):
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi, cong_viec):
        super().__init__(ho_ten, tuoi, gioi_tinh, dia_chi)
        self.cong_viec = cong_viec

    def mo_ta(self):
        return f"Nhan vien: {self.cong_viec}"

    def __str__(self):
        return super().__str__() + f" | {self.mo_ta()}"

class FileCanBoManager:
    def __init__(self, filename):
        self.filename = filename
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, 'a+', encoding='utf-8')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()

if __name__ == "__main__":
    try:
        cn = CongNhan("Nguyen Van A", 30, "Nam", "Ha Noi", 5)
        ks = KySu("Tran Thi B", 25, "Nu", "Da Nang", "Co khi")
        nv = NhanVien("Le Van C", 40, "Nam", "HCM", "Ke toan")

        danh_sach = [cn, ks, nv]
        danh_sach.sort()

        with FileCanBoManager("danh_sach_can_bo.txt") as f:
            for cb in danh_sach:
                print(cb)
                f.write(str(cb) + "\n")

    except (TuoiKhongHopLe, BacKhongHopLe) as e:
        print(f"Loi du lieu: {e}")
    except Exception as e:
        print(f"Loi: {e}")
