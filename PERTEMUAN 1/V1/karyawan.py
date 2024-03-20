class Karyawan:
    def __init__(self, nama, jabatan):
        self.nama = nama
        self.jabatan = jabatan
        
    def info(self):
        print(f"Nama: {self.nama}\nJabatan: {self.jabatan}")
        
karyawan1 = Karyawan("Riski", "Programer")
karyawan1.info()
