while True:
    try:
        input_angka = float(input("masukan angka: "))
        break  
    except ValueError:
        print("Error: masukan harus berupa angka")
        

print("angka yang dimasukan:", input_angka)
