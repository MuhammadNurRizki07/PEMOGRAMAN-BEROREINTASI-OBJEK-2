def hitung_limas_segiempat():
    try:
        sisi_alas = float(input("Masukkan panjang sisi alas: "))
        tinggi_limas = float(input("Masukkan tinggi limas: "))
        tinggi_segitiga = float(input("Masukkan tinggi segitiga: "))
        
        assert sisi_alas > 0 and tinggi_limas > 0 and tinggi_segitiga > 0
        
        luas = round(sisi_alas ** 2) + 2 * sisi_alas * (tinggi_limas + tinggi_segitiga)
        volume = round(sisi_alas ** 2 * tinggi_limas) / 3
        
        print("Luas Limas Segiempat:", luas)
        print("Volume Limas Segiempat:", volume)
    except ValueError:
        print("Error: Masukan harus berupa angka")
    except AssertionError:
        print("Error: Angka tidak boleh nol atau negatif")

hitung_limas_segiempat()
