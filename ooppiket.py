#==============================
# APLIKASI PIKET KELAS
#==============================

class Piket:
    def __init__(self, nama_siswa, kelas):
        self.nama_siswa = nama_siswa
        self.kelas = kelas
        self.hadir = False
    
    def absen(self, status):
        self.hadir = status

class PiketKelas:
    def __init__(self, hari):
        self.hari = hari
        self.daftar_siswa =[]

    def tambah_siswa(self,siswa):
        self.daftar_siswa.append(siswa)

    def absen_siswa(self):
        print(f"\nAbsen Piket Hari {self.hari}")
        for siswa in self.daftar_siswa:
            status = input(f"Apakah {siswa.nama_siswa} hadir dan melaksanakan piket hari ini? (y/n): ")
            if status.lower() == "y":
                siswa.absen (True)
                print(f"✓ {siswa.nama_siswa} Hadir")
            else:
                siswa.absen (False)
                print(f"✗ {siswa.nama_siswa} Tidak Hadir")

    def tampilkan_piket(self):
        print(f"\nDaftar Piket Hari ini {self.hari}:")
        for siswa in self.daftar_siswa:
            status = "Hadir" if siswa.hadir else "Tidak Hadir"
            print(f" - {siswa.nama_siswa} ({siswa.kelas}) : {status}")

#====================
# PROGRAM UTAMA
#====================

piket_senin = PiketKelas("Senin")
siswa1 = Piket("Andi", "10 MP 1")
siswa2 = Piket("Budi", "10 MP 1")
siswa3 = Piket("Citra", "10 MP 1")
siswa4 = Piket("Sarah", "10 MP 1")
siswa5 = Piket("Dina", "10 MP 1")
piket_senin.tambah_siswa(siswa1)
piket_senin.tambah_siswa(siswa2)
piket_senin.tambah_siswa(siswa3)
piket_senin.tambah_siswa(siswa4)
piket_senin.tambah_siswa(siswa5)

piket_senin.absen_siswa()
piket_senin.tampilkan_piket()