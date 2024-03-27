try:
    pilihan=int (input('masukan angka lebih dari 0:'))
    assert pilihan > 0 
except AssertionError :
    print ("angka tidak boleh nol atau negatif")