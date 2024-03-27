while True:
    try:
        suhu_celsius = float(input("Masukkan suhu dalam derajat Celsius: "))
        
        suhu_fahrenheit = (suhu_celsius * 9/5) + 32
        
        print("Suhu dalam Fahrenheit:", suhu_fahrenheit)
        break
    except ValueError:
        print("Error: Masukan harus berupa angka")
