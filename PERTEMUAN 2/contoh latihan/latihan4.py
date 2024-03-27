try:
    f=open("file.txt","r")
except FileNotFoundError:
    print("file tidak ditemukan")    