def hitung_persegi_panjang():
    try:
        panjang = float(input("Masukkan panjang persegi panjang: "))
        lebar = float(input("Masukkan lebar persegi panjang: "))
        
        assert panjang > 0 and lebar > 0
        
        luas = panjang * lebar
        keliling = 2 * (panjang + lebar)
        
        print("Luas Persegi Panjang:", luas)
        print("Keliling Persegi Panjang:", keliling)
    except ValueError:
        print("Error: Masukan harus berupa angka")
    except AssertionError:
        print("Error: Panjang dan lebar tidak boleh nol atau negatif")


hitung_persegi_panjang()
