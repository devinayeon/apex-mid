angka = {
    1: "Layanan Peminjaman Buku",
    2: "Layanan Pengembalian Buku",
    3: "Layanan Perpanjangan peminjaman",
    4: "Layanan Informasi keanggotaan"
}

pilih = int(input())

if pilih in angka:
    print(f"{angka[pilih]}")
else:
    print("Layanan tidak ditemukan")