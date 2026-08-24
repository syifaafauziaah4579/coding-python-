class Kalkulator:
    def __init__(self):
        self.angka1 = 0
        self.angka2 = 0
        self.angka3 = 0
        self.angka4 = 0
        self.angka5 = 0
        self.hasil = 0
    
    def tambah(self):
        self.hasil = self.angka1 + self.angka2 + self.angka3 + self.angka4 + self.angka5
        return self.hasil
    
    def kurang(self):
        self.hasil = self.angka1 - self.angka2 - self.angka3 - self.angka4 - self.angka5
        return self.hasil
    def kali(self):
        self.hasil = self.angka1 * self.angka2 * self.angka3 * self.angka4 * self.angka5
        return self.hasil
    
    def bagi(self):
        self.hasil = self.angka1 / self.angka2 / self.angka3 / self.angka4 / self.angka5
        return self.hasil
    
Kalkulator = Kalkulator()
Kalkulator.angka1 = 20
Kalkulator.angka2 = 2
Kalkulator.angka3 = 5
Kalkulator.angka4 = 18
Kalkulator.angka5 = 7
print(Kalkulator.tambah())

Kalkulator.angka1 = 9
Kalkulator.angka2 = 2
Kalkulator.angka3 = 8
Kalkulator.angka4 = 7
Kalkulator.angka5 = 3
print(Kalkulator.kurang())

Kalkulator.angka1 = 34
Kalkulator.angka2 = 10
Kalkulator.angka3 = 0
Kalkulator.angka4 = 2
Kalkulator.angka5 = 6
print(Kalkulator.kali())

Kalkulator.angka1 = 10
Kalkulator.angka2 = 2
Kalkulator.angka3 = 1
Kalkulator.angka4 = 5
Kalkulator.angka5 = 9
print(Kalkulator.bagi())