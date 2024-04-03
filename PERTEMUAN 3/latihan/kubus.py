class Kubus:
    def __init__(self, sisi):
        self.__set_sisi(sisi)

    def get_sisi(self):
        return self.__sisi

    def __set_sisi(self, nilai):
        self.__sisi = 1 if nilai <= 0 else nilai

    def luas_permukaan(self):
        return 6 * self.__sisi ** 2

    def volume(self):
        return self.__sisi ** 3

try:
    sisi = float(input("Masukkan panjang sisi kubus: "))
except ValueError:
    print("Masukkan hanya angka saja.")
else:
    kubus = Kubus(sisi)
    luas_permukaan = kubus.luas_permukaan()
    volume = kubus.volume()
    print("Sisi Kubus:", kubus.get_sisi())
    print("Luas Permukaan Kubus:", luas_permukaan)
    print("Volume Kubus:", volume)
