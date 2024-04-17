class person:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

class Dosen(person):
    def __init__(self, nama, umur, nidn, fakultas, prodi, jabatan_akademik, jabatan_struktural):
        super().__init__(nama, umur)
        self.nidn = nidn
        self.fakultas = fakultas
        self.prodi = prodi
        self.jabatan_akademik = jabatan_akademik
        self.jabatan_struktural = jabatan_struktural

class Mahasiswa(person):
    def __init__(self, nama, umur, nim, fakultas, prodi, angkatan):
        super().__init__(nama, umur)
        self.nim = nim
        self.fakultas = fakultas
        self.prodi = prodi
        self.angkatan = angkatan

class Staff(person):
    def __init__(self, nama, umur, departemen, jabatan):
        super().__init__(nama, umur)
        self.departemen = departemen
        self.jabatan = jabatan

class Satpam(person):
    def __init__(self, nama, umur, lokasi_jaga):
        super().__init__(nama, umur)
        self.lokasi_jaga = lokasi_jaga

class OB(person):
    def __init__(self, nama, umur, tugas):
        super().__init__(nama, umur)
        self.tugas = tugas

if __name__ == "__main__":
    dosen = Dosen("Prof. Dr. Ahmad", 45, "123456789", "Fakultas Teknik", "Teknik Informatika", "Guru Besar", "Ketua Program Studi")
    print("\nDosen:")
    print("Nama:", dosen.nama)
    print("Umur:", dosen.umur)
    print("NIDN:", dosen.nidn)
    print("Fakultas:", dosen.fakultas)
    print("Program Studi:", dosen.prodi)
    print("Jabatan Akademik:", dosen.jabatan_akademik)
    print("Jabatan Struktural:", dosen.jabatan_struktural)

    mahasiswa = Mahasiswa("Ani", 20, "123456789", "Fakultas Ekonomi", "Manajemen", 2023)
    print("\nMahasiswa:")
    print("Nama:", mahasiswa.nama)
    print("Umur:", mahasiswa.umur)
    print("NIM:", mahasiswa.nim)
    print("Fakultas:", mahasiswa.fakultas)
    print("Program Studi:", mahasiswa.prodi)
    print("Angkatan:", mahasiswa.angkatan)

    staff = Staff("Budi", 30, "Keuangan", "Administrasi")
    print("\nStaff:")
    print("Nama:", staff.nama)
    print("Umur:", staff.umur)
    print("Departemen:", staff.departemen)
    print("Jabatan:", staff.jabatan)

    satpam = Satpam("Joko", 35, "Gedung A")
    print("\nSatpam:")
    print("Nama:", satpam.nama)
    print("Umur:", satpam.umur)
    print("Lokasi Jaga:", satpam.lokasi_jaga)

    ob = OB("Siti", 25, "Kebersihan")
    print("\nOffice Boy:")
    print("Nama:", ob.nama)
    print("Umur:", ob.umur)
    print("Tugas:", ob.tugas)
