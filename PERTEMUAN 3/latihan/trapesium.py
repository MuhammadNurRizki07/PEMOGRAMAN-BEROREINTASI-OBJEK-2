class Trapesium:
    def __init__(self, alas_atas, alas_bawah, tinggi, sisi_miring):
        self.__set_alas_atas(alas_atas)
        self.__set_alas_bawah(alas_bawah)
        self.__set_tinggi(tinggi)
        self.__set_sisi_miring(sisi_miring)

    def get_alas_atas(self):
        return self.__alas_atas

    def get_alas_bawah(self):
        return self.__alas_bawah

    def get_tinggi(self):
        return self.__tinggi

    def get_sisi_miring(self):
        return self.__sisi_miring

    def __set_alas_atas(self, nilai):
        self.__alas_atas = 1 if nilai <= 0 else nilai

    def __set_alas_bawah(self, nilai):
        self.__alas_bawah = 1 if nilai <= 0 else nilai

    def __set_tinggi(self, nilai):
        self.__tinggi = 1 if nilai <= 0 else nilai

    def __set_sisi_miring(self, nilai):
        self.__sisi_miring = 1 if nilai <= 0 else nilai

    def luas(self):
        return (self.__alas_atas + self.__alas_bawah) * self.__tinggi / 2

    def keliling(self):
        return self.__alas_atas + self.__alas_bawah + 2 * self.__sisi_miring

try:
    alas_atas = int(input("Masukkan nilai alas atas: "))
    alas_bawah = int(input("Masukkan nilai alas bawah: "))
    tinggi = int(input("Masukkan nilai tinggi: "))
    sisi_miring = int(input("Masukkan nilai sisi miring: "))
except ValueError:
    print("Masukkan hanya angka saja.")
else:
    t = Trapesium(alas_atas, alas_bawah, tinggi, sisi_miring)
    L = t.luas()
    k = t.keliling()
    print("Alas Atas:", t.get_alas_atas())
    print("Alas Bawah:", t.get_alas_bawah())
    print("Tinggi:", t.get_tinggi())
    print("Sisi Miring:", t.get_sisi_miring())
    print("Luas Trapesium:", L)
    print("Keliling Trapesium:", k)
