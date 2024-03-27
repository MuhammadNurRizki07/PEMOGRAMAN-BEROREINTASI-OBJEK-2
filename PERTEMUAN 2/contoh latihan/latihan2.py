def hitung_akar_kuadrat(angka):
    if angka < 0:
        raise ValueError("Angka tidak boleh negatif")
    return angka ** 0.5

try:
    nilai_angka = float(input("Masukkan nilai angka non-negatif: "))
    hasil_akar = hitung_akar_kuadrat(nilai_angka)
    print("Akar kuadrat dari", nilai_angka, "adalah", hasil_akar)
except ValueError as e:
    print("Pesan kesalahan:", e)
