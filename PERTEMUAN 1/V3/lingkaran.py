class Lingkaran:
    def __init__(self):
        self.jari_jari = None
        self.luas = None
        self.keliling = None
        
    @property
    def jari_jari(self):
        return self._jari_jari
    
    @jari_jari.setter
    def jari_jari(self, value):
        self._jari_jari = value
        
    def hitung_luas(self):
        self.luas = 3.14 * self._jari_jari ** 2
        return self.luas
    
    def hitung_keliling(self):
        self.keliling = 2 * 3.14 * self._jari_jari
        return self.keliling
    
lingkaran = Lingkaran()

jari_jari = float(input("Masukkan jari-jari lingkaran: "))

lingkaran.jari_jari = jari_jari

luas = lingkaran.hitung_luas()
keliling = lingkaran.hitung_keliling()

print("Jari-jari lingkaran:", jari_jari)
print("Luas lingkaran:", luas)
print("Keliling lingkaran:", keliling)
