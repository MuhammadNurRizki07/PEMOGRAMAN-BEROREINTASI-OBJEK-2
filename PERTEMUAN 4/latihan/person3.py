class Person:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

class Manager(Person):
    def __init__(self, nama, umur, divisi, idmanager):
        super().__init__(nama, umur)
        self.divisi = divisi
        self.idmanager = idmanager

class Programmer(Person):
    def __init__(self, nama, umur, posisi, id_programer):
        super().__init__(nama, umur)
        self.posisi = posisi
        self.idprogramer = id_programer

class Staff(Person):
    def __init__(self, nama, umur, jabatan, idmanager):
        super().__init__(nama, umur)
        self.jabatan = jabatan
        self.idmanager = idmanager

class Teknisi(Person):
    def __init__(self, nama, umur, divisi, idmanager):
        super().__init__(nama, umur)
        self.divisi = divisi
        self.idmanager = idmanager

if __name__ == "__main__":
    manager = Manager("Muhammad Nur Rizki", 20, "keuangan", "220511028")
    print("Manager:")
    print("Nama:", manager.nama)
    print("Umur:", manager.umur)
    print("Divisi:", manager.divisi)
    print("ID Manager:", manager.idmanager)
    
    programmer = Programmer("Iki", 19, "Backend Developer", "12345")
    print("\nProgrammer:")
    print("Nama:", programmer.nama)
    print("Umur:", programmer.umur)
    print("Posisi:", programmer.posisi)
    print("ID Programmer:", programmer.idprogramer)

    staff = Staff("rinaa", 19, "HR Assistant", "54321")
    print("\nStaff:")
    print("Nama:", staff.nama)
    print("Umur:", staff.umur)
    print("Jabatan:", staff.jabatan)
    print("ID Manager:", staff.idmanager)

    teknisi = Teknisi("riski", 35, "IT Support", "67890")
    print("\nTeknisi:")
    print("Nama:", teknisi.nama)
    print("Umur:", teknisi.umur)
    print("Divisi:", teknisi.divisi)
    print("ID Manager:", teknisi.idmanager)
