def ambil_nilai(kamus,kunci):
    try:
        nilai = kamus[kunci]
        print ("nilai dari kunci",kunci,"adalah", nilai)
    except KeyError:
        print("Error: kunci",kunci,"tidak ditemukan dalam kamus")
data = {'nama': 'jhon', 'usia': 30, 'kota': 'jakarta'}
kunci = input("masukan kunci [nama,usia,kota]:")
ambil_nilai(data,kunci)        