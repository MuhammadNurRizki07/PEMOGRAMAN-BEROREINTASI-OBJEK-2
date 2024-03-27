while True:
    try:
        angka = int(input("Masukkan bilangan bulat positif: "))
        if angka <= 0:
            raise ValueError("Angka harus lebih besar dari 0")
        
        faktorial = 1
        for i in range(1, angka + 1):
            faktorial *= i
        
        print("Faktorial dari", angka, "adalah:", faktorial)
        break
    except ValueError as e:
        print("Error: harus berupa angka:", e)
