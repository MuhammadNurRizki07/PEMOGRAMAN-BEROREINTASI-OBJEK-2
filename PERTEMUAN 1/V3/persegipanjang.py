class PersegiPanjang:
    def __init__(self):
        self._panjang = None
        self._lebar = None
        
    @property
    def panjang(self):
        return self._panjang
    
    @panjang.setter
    def panjang(self, value):
        self._panjang = value
        
    @property
    def lebar(self):
        return self._lebar
    
    @lebar.setter
    def lebar(self, value):
        self._lebar = value
        
    def luas(self):
        return self._panjang * self._lebar
    
    def keliling(self):
        return 2 * (self._panjang + self._lebar)
    
PP = PersegiPanjang()
P = float(input("Masukkan nilai panjang: "))
L = float(input("Masukkan nilai lebar: "))

PP.panjang = P
PP.lebar = L

luas = PP.luas()
keliling = PP.keliling()

print("Panjang:", P)
print("Lebar:", L)
print("Luas:", luas)
print("Keliling:", keliling)
