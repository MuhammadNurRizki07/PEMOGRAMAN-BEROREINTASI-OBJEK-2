def hitung_persegi():
    try:
        sisi = float(input("Masukkan panjang sisi persegi: "))
        
        assert sisi > 0
        
        luas = sisi ** 2
        keliling = 4 * sisi
        
        print("Luas Persegi:", luas)
        print("Keliling Persegi:", keliling)
    except ValueError:
        print("Error: Masukan harus berupa angka")
    except AssertionError:
        print("Error: Panjang sisi tidak boleh nol atau negatif")

# Jalankan fungsi hitung_persegi
hitung_persegi()
