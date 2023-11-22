#  Tugas Punya : Eko Muchamad Haryono
#  TI - 02
#  Teknik Informatika
#  Dasar - Dasar Pemograman (DDP)
#  Tema : Kerjakan Soal Pertemuan - 7, Menggunakan Python --> Latihan UTS

# Soal Quiz 
# 1. Buatlah sebuah flowchart dan program dengan bahasa python ketentuan sebagai berikut : 
# Jenis bensin = Pertalite - Pertamax - Pertamax Turbo 
# Harga = 10000 / liter - 14000 / liter - 17000 / liter
# Jarak tempuh = 12 KM - 13 KM - 13.5 KM

# Tentukan berapa rupiah yang dikeluarkan kalian untuk jalan jalan ke kota berikut ini : 
# Kota = Jakarta - Bekasi - Depok - Tangerang - Bogor 
# Jarak = 20 KM - 35.7 KM - 5 KM - 99 KM - 120.6 KM

# Dengan Inputan : 
# Nama kendaraan ? contoh : {mobil, motor}
# Jenis bensin ? 
# Kota yang di tuju?

# Dengan Outputan : 
# Nama Kendaraan 
# Jenis Bensin 
# Kota yang dituju 
# Pemakaian bensin?  (jarak kota dibagi  jarak tempuh jenis bensin)
# Total Harga dari bensin ?  (pemakaian bensin dikalikan harga perliter)

# Syntax Nomer 1 :
# Input jenis bensin, harga, dan jarak tempuh
# Input dari pengguna
print("\n","1. Hasil Inputan Tugas Nomer 1 :")
nama_kendaraan = input("Nama kendaraan (mobil/motor): ")
jenis_bensin_lower = input("Jenis bensin (Pertalite/Pertamax/Pertamax Turbo): ")
kota_tujuan_lower = input("Kota tujuan (Jakarta/Bekasi/Depok/Tangerang/Bogor): ")

jenis_bensin = jenis_bensin_lower.lower()
kota_tujuan = kota_tujuan_lower.lower()

# Menentukan harga dan jarak tempuh berdasarkan jenis bensin
if jenis_bensin == "pertalite":
    harga_per_liter = 10000
    jarak_tempuh = 12
elif jenis_bensin == "pertamax":
    harga_per_liter = 14000
    jarak_tempuh = 13
elif jenis_bensin == "pertamax turbo":
    harga_per_liter = 17000
    jarak_tempuh = 13.5
else:
    print("Jenis bensin tidak valid")
    exit()

# Menentukan jarak berdasarkan kota tujuan
if kota_tujuan == "jakarta":
    jarak = 20
elif kota_tujuan == "bekasi":
    jarak = 35.7
elif kota_tujuan == "depok":
    jarak = 5
elif kota_tujuan == "tangerang":
    jarak = 99
elif kota_tujuan == "bogor":
    jarak = 120.6
else:
    print("Kota tujuan tidak valid")
    exit()

# Menghitung pemakaian bensin dan total harga
pemakaian_bensin = jarak / jarak_tempuh
total_harga = pemakaian_bensin * harga_per_liter

# Hasil Output Tugas 1
print()
print("1. Hasil Outputan Tugas Nomer 1 :")
print("Nama Kendaraan: ", nama_kendaraan)
print("Jenis Bensin:", jenis_bensin)
print("Kota yang Dituju:", kota_tujuan)
print("Pemakaian Bensin:", round(pemakaian_bensin, 2), "liter")
print("Total Harga dari Bensin:", round(total_harga, 2), "rupiah")
print()


# Syntax Nomer 2 :
# Tampilkan Menu Makanan dan Minuman
menu_makanan = {
    "Nasi Goreng": 15000,
    "Mie Goreng": 12000,
    "Ayam Geprek": 18000
}

menu_minuman = {
    "Aneka Jus": 15000,
    "Soft Drink": 10000,
    "Sweet Ice Tea": 5000
}

# Input Nama Pembeli dan No Hp Pembeli
nama_pembeli = input("Masukkan Nama Pembeli: ")
no_hp_pembeli = input("Masukkan No Hp Pembeli: ")

# Pesan Menu Makanan atau Minuman
jenis_pesanan = input("Pesan Menu Apa? (makanan atau minuman): ")

# Tampilkan Menu Sesuai Jenis Pesanan
if jenis_pesanan.lower() == "makanan":
    print("Menu Makanan:")
    for menu, harga in menu_makanan.items():
        print(f"{menu} - Rp. {harga}")
    pesanan = input("Masukkan pesanan: ")
    harga_pesanan = menu_makanan.get(pesanan, 0)
elif jenis_pesanan.lower() == "minuman":
    print("Menu Minuman:")
    for menu, harga in menu_minuman.items():
        print(f"{menu} - Rp. {harga}")
    pesanan = input("Masukkan pesanan: ")
    harga_pesanan = menu_minuman.get(pesanan, 0)
else:
    print("Jenis pesanan tidak valid. Silakan pilih makanan atau minuman.")
    exit()

# Input Jumlah Pesanan
jumlah_pesanan = int(input("Masukkan Jumlah Pesanan: "))

# Hitung Harga Total
harga_total = harga_pesanan * jumlah_pesanan

# Output Informasi Pemesanan
print("\nInformasi Pemesanan:")
print(f"Nama Pembeli: {nama_pembeli}")
print(f"No Hp Pembeli: {no_hp_pembeli}")
print(f"Menu yang di Pesan: {pesanan}")
print(f"Jumlah Pesanan: {jumlah_pesanan}")
print(f"Harga yang harus di bayarkan: Rp. {harga_total}")



# Syntax Nomer 3 :
for i in range(1, 21):
    if i % 3 == 0 and i % 5 != 0:
        print("STT Nurul Fikri")
    else:
        print(i)
        
#  Tugas Punya : Eko Muchamad Haryono
#  TI - 02
#  Teknik Informatika
#  Dasar - Dasar Pemograman (DDP)
#  Tema : Kerjakan Soal Pertemuan - 7, Menggunakan Python 
