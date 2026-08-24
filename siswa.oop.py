class Siswa:
    def __init__(self):
        # Properti ini opsional jika data diambil dari list eksternal
        self.nama = "" 
        self.umur = ""
        self.agama = ""

    def absen(self, daftar_siswa):
        print("=== SISTEM ABSEN SCANNER ===")
        inputid = input("Scan Kartu Absen (Masukkan ID):")

        #Variabel untuk menandai apakah siswa ditemukan
        ditemukan = False

        for s in daftar_siswa:
            if s["idcrad"] == inputid:
                print("/n✅ ABSENSI BERHASIL")
                print(f"Nama : {s['nama']}")
                print(f"Umur : {s['umur']}")
                print(f"Agama : {s['agama']}")
                print(f"Status : Sudah Absen")
                ditemuka = True
                break # Berhenti mencari jika sudah ketemu
        
        if not ditemukan:
            print("/n❌ Siswa belum absen / ID tidak terdaftar!")
           
data = [
    {"nama": "Budi", "umur": "15", "agama": "Islam", "idcrad": "030729"},
    {"nama": "Siti", "umur": "16", "agama": "Kristen", "idcrad": "030730"}
]
#Jalankan program
siswa = Siswa()
siswa.absen(data)