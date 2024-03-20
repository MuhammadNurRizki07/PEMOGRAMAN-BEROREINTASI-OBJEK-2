class Lagu:
    def __init__(self, judul, penyanyi, album, tahun_rilis):
        self.judul = judul
        self.penyanyi = penyanyi
        self.album = album
        self.tahun_rilis = tahun_rilis
        
    def info(self):
        print(f"Judul: {self.judul}\nPenyanyi: {self.penyanyi}\nAlbum: {self.album}\nTahun Rilis: {self.tahun_rilis}")

lagu1 = Lagu("Shape of You", "Ed Sheeran", "Divide", 2017)
lagu1.info()
