try:
    pilihan = int (input('masukan angka:'))
    assert pilihan > 0 
except AssertionError:
    print("angka tidak boleh nol atau negative")
except ValueError:
    print("input harus angka")