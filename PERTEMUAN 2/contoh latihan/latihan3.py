try:
    a=[1,2,3]
    b=int(input("masukan nomor index[0,1,2]:"))
    print(a[b])
except IndexError:
    print("index diluar rentang array")
except Exception as e:
    print("terjadi kesalahan", e)