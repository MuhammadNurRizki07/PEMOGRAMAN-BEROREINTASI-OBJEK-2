def minta_input(pesan):
    while True:
        try:
            nilai_input = input(pesan)
            if nilai_input.strip() == "": 
                raise ValueError("Input harus tidak boleh kosong")
            nilai_numerik = float(nilai_input)  
            return nilai_numerik
        except ValueError as e:
            print(e)

angka1 = minta_input("Masukkan angka pertama: ")
angka2 = minta_input("Masukkan angka kedua: ")

hasil = angka1 + angka2
print(f"Hasil penjumlahan {angka1} dan {angka2} adalah {hasil}")
