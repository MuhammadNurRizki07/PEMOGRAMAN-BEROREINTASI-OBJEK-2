class Tabung:
    def __init__(self):
        self.jari_jari = None
        self.tinggi = None
        self.luas_permukaan = None
        self.volume = None
        
    def hitung_luas_permukaan(self, jari_jari, tinggi):
        self.jari_jari = jari_jari 
        self.tinggi = tinggi
        self.luas_permukaan = 2 * 3.14 * self.jari_jari * (self.jari_jari + self.tinggi)  # Menggunakan nilai pi perkiraan
        return self.luas_permukaan
    
    def hitung_volume(self, jari_jari, tinggi):
        self.jari_jari = jari_jari 
        self.tinggi = tinggi
        self.volume = 3.14 * self.jari_jari**2 * self.tinggi  # Menggunakan nilai pi perkiraan
        return self.volume
    
t = Tabung()

jari_jari = float(input("Masukkan jari-jari tabung: "))
tinggi = float(input("Masukkan tinggi tabung: "))

luas_permukaan = t.hitung_luas_permukaan(jari_jari, tinggi)
volume = t.hitung_volume(jari_jari, tinggi)

print("Jari-jari:", jari_jari)
print("Tinggi:", tinggi)
print("Luas Permukaan Tabung:", luas_permukaan)
print("Volume Tabung:", volume)
