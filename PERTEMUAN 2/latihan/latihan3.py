while True:
    try:
        angka1 = float(input("Masukkan angka pertama: "))
        angka2 = float(input("Masukkan angka kedua: "))
        
        total = angka1 + angka2
        
        print("Hasil penjumlahan:", total)
        break
    except ValueError:
        print("Error: Masukan harus berupa angka")
