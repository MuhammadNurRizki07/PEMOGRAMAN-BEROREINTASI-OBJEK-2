class person:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

class Dokter(person):
    def __init__(self, nama, umur, spesialisasi, nomor_str):
        super().__init__(nama, umur)
        self.spesialisasi = spesialisasi
        self.nomor_str = nomor_str

class Perawat(person):
    def __init__(self, nama, umur, bidang, nomor_registrasi):
        super().__init__(nama, umur)
        self.bidang = bidang
        self.nomor_registrasi = nomor_registrasi

class Karyawan(person):
    def __init__(self, nama, umur, departemen, nomor_pegawai):
        super().__init__(nama, umur)
        self.departemen = departemen
        self.nomor_pegawai = nomor_pegawai

if __name__ == "__main__":
    dokter = Dokter("dr. Riski", 20, "Bedah Umum", "12345")
    print("\nDokter:")
    print("Nama:", dokter.nama)
    print("Umur:", dokter.umur)
    print("Spesialisasi:", dokter.spesialisasi)
    print("Nomor STR:", dokter.nomor_str)

    perawat = Perawat("Suster young jun", 35, "ICU", "54321")
    print("\nPerawat:")
    print("Nama:", perawat.nama)
    print("Umur:", perawat.umur)
    print("Bidang:", perawat.bidang)
    print("Nomor Registrasi:", perawat.nomor_registrasi)

    karyawan = Karyawan("Han so he", 25, "Keuangan", "67890")
    print("\nKaryawan:")
    print("Nama:", karyawan.nama)
    print("Umur:", karyawan.umur)
    print("Departemen:", karyawan.departemen)
    print("Nomor Pegawai:", karyawan.nomor_pegawai)
