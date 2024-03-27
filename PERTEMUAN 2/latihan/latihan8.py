import math

def minta_input(pesan):
    while True:
        try:
            nilai_input = input(pesan)
            if nilai_input.strip() == "": 
                raise ValueError("Input harus tidak boleh kosong")
            nilai_numerik = float(nilai_input) 
            if nilai_numerik <= 0: 
                raise ValueError("Jari-jari harus lebih besar dari 0")
            return nilai_numerik
        except ValueError as e:
            print(e)

jari_jari = minta_input("Masukkan jari-jari lingkaran: ")

luas = math.pi * jari_jari ** 2
print(f"Luas lingkaran dengan jari-jari {jari_jari} adalah {luas:.2f}")
