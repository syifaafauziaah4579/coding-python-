  # Studi Kasus: Manajemen Inventaris Toko

inventaris = [
    {"nama": "piring", "stok": 10, "harga": 20000},
    {"nama": "gelas", "stok": 20, "harga": 10000},
]

def tampilkan_produk():
    print("=== Daftar Produk ===")
    for produk in inventaris:
        print(f"{produk['nama']} - Stok: {produk['stok']} - Harga: {produk['harga']}")

def tambah_produk(nama, stok, harga):
    inventaris.append({"nama": nama, "stok": stok, "harga": harga})
    print(f"Produk {nama} berhasil ditambahkan!")

tampilkan_produk()
tambah_produk("sendok", 10, 15000)
tampilkan_produk()