class Hewan:
    def __init__(self, nama, jenis, berat, tinggi):
        self.nama = nama
        self.berat = berat
        self.tinggi = tinggi

    def a(self):
        print("hewan ini berjalan")

gajah = Hewan("gajah", "mamalia", "2 ton", "3 meter")

print(gajah.nama)
print(gajah.berat)
print(gajah.tinggi)

gajah.a() 