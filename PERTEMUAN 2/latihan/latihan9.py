def minta_input(pesan):
    while True:
        try:
            nilai_input = input(pesan)
            if nilai_input.strip() == "":
                raise ValueError("Input harus tidak boleh kosong")
            nilai_numerik = float(nilai_input) 
            if nilai_numerik <= 0:  
                raise ValueError("Nilai harus lebih besar dari 0")
            return nilai_numerik
        except ValueError as e:
            print(e)


sisi = minta_input("Masukkan panjang sisi persegi (cm): ")

luas = sisi * sisi
keliling = 4 * sisi

print(f"Luas persegi dengan sisi {sisi} cm adalah {luas} cm^2.")
print(f"Keliling persegi dengan sisi {sisi} cm adalah {keliling} cm.")
