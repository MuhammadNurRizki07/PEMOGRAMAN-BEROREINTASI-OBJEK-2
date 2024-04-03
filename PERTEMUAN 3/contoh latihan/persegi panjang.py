class PersegiPanjang:
    def __init__(self, panjang, lebar):
        self.__set_panjang(panjang)
        self.__set_lebar(lebar)

    def get_panjang(self):
        return self.__panjang

    def get_lebar(self):
        return self.__lebar

    def __set_panjang(self, nilai):
        self.__panjang = 1 if nilai <= 0 else nilai

    def __set_lebar(self, nilai):
        self.__lebar = 1 if nilai <= 0 else nilai

    def luas(self):
        return self.__panjang * self.__lebar

    def keliling(self):
        return 2 * (self.__panjang + self.__lebar)

try:
    panjang = int(input("Masukkan nilai panjang: "))
    lebar = int(input("Masukkan nilai lebar: "))
except ValueError:
    print("Masukkan hanya angka saja.")
else:
    p = PersegiPanjang(panjang, lebar)
    L = p.luas()
    k = p.keliling()
    print("Panjang:", p.get_panjang())
    print("Lebar:", p.get_lebar())
    print("Luas Persegi Panjang:", L)
    print("Keliling Persegi Panjang:", k)
