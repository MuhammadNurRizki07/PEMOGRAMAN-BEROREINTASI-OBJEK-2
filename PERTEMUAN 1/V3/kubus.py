class Kubus:
    def __init__(self):
        self.sisi = None
        self.luas_permukaan = None
        self.volume = None
        
    @property
    def sisi(self):
        return self._sisi
    
    @sisi.setter
    def sisi(self, value):
        self._sisi = value
        
    def hitung_luas_permukaan(self):
        self.luas_permukaan = 6 * self._sisi ** 2
        return self.luas_permukaan
    
    def hitung_volume(self):
        self.volume = self._sisi ** 3
        return self.volume
    
kubus = Kubus()

sisi = float(input("Masukkan panjang sisi kubus: "))

kubus.sisi = sisi

luas_permukaan = kubus.hitung_luas_permukaan()
volume = kubus.hitung_volume()

print("Sisi kubus:", sisi)
print("Luas permukaan kubus:", luas_permukaan)
print("Volume kubus:", volume)
