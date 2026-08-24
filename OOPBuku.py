class Buku:
#properti
    def __init__(self):
        self.penerbit =""
        self.penulis =""
    
#method/funcition
    def dibaca (self):
        print("Buku sedang dibaca")
    
Buku1 = Buku()
Buku1.penerbit ="Granmedia"
Buku1.penulis ="Suga"

print(f"Penerbit: {Buku1.penerbit} dan Penulis: {Buku1.penulis}")

Buku2 = Buku()
Buku2.penerbit ="Elex Media Komputindo"
Buku2.penulis ="Andi Prasetyo"

print(f"Penerbit: {Buku2.penerbit} dan Penulis: {Buku2.penulis}")