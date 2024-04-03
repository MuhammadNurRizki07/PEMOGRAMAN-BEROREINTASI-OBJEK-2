class BelahKetupat:
    def __init__(self, diagonal1, diagonal2, sisi):
        self.__set_diagonal1(diagonal1)
        self.__set_diagonal2(diagonal2)
        self.__set_sisi(sisi)

    def __set_diagonal1(self, nilai):
        self.__diagonal1 = 1 if nilai <= 0 else nilai

    def __set_diagonal2(self, nilai):
        self.__diagonal2 = 1 if nilai <= 0 else nilai

    def __set_sisi(self, nilai):
        self.__sisi = 1 if nilai <= 0 else nilai

    def get_diagonal1(self):
        return self.__diagonal1

    def get_diagonal2(self):
        return self.__diagonal2

    def get_sisi(self):
        return self.__sisi

    def luas(self):
        return 0.5 * self.__diagonal1 * self.__diagonal2

    def keliling(self):
        return 4 * self.__sisi

try:
    diagonal1 = float(input("Masukkan panjang diagonal 1: "))
    diagonal2 = float(input("Masukkan panjang diagonal 2: "))
    sisi = float(input("Masukkan panjang sisi belah ketupat: "))
except ValueError:
    print("Masukkan hanya angka saja.")
else:
    belah_ketupat = BelahKetupat(diagonal1, diagonal2, sisi)
    luas = belah_ketupat.luas()
    keliling = belah_ketupat.keliling()
    print("Diagonal 1 Belah Ketupat:", belah_ketupat.get_diagonal1())
    print("Diagonal 2 Belah Ketupat:", belah_ketupat.get_diagonal2())
    print("Sisi Belah Ketupat:", belah_ketupat.get_sisi())
    print("Luas Belah Ketupat:", luas)
    print("Keliling Belah Ketupat:", keliling)
