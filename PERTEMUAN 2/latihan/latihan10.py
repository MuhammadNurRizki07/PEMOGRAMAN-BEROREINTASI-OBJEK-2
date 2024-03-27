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

bilangan1 = minta_input("Masukkan bilangan pertama: ")
bilangan2 = minta_input("Masukkan bilangan kedua: ")

hasil = bilangan1 * bilangan2

print(f"Hasil perkalian {bilangan1} dan {bilangan2} adalah {hasil}.")
