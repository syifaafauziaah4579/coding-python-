class Buah:
    def __init__(self, nama, rasa, harga):
        self.nama = nama
        self.rasa = rasa
        self.harga = harga

    def a(self):
        print("buah ini dimakan")

mangga = Buah("mangga", "manis", 20000)

print(mangga.nama)
print(mangga.rasa)
print(mangga.harga)

mangga.a() 