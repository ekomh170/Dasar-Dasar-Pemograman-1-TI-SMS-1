#  Tugas Punya : Eko Muchamad Haryono
#  TI - 02
#  Teknik Informatika
#  Dasar - Dasar Pemograman (DDP)
#  Tema : Kerjakan Soal Pertemuan - 5, Menggunakan Python

# Lets  Code
# Kerjakan Soal Pertemuan - 5
# Tanggal : 25 - 10 - 2023

# 1. - Buat variabel List Dengan Value : [namaKendaraan, JenisKendaraan, ccKendaraan. warna kendaraan, roda kendaraan]
# - Tambahkan dari list tersebut di belakang dengan value : [harga kendaraan, tipe kendaraan]
# - Tambahkan setelah jenis kendaraan dengan value [merk kendaraan]
# =============================================================

# - Buat variabel List Dengan Value : [namaKendaraan, JenisKendaraan, ccKendaraan. warna kendaraan, roda kendaraan]
listVariabelKendaraan = ["BMW M3 GTR E46", "Mobil", 3700, "Biru", 4]

# - Tambahkan dari list tersebut di belakang dengan value : [harga kendaraan, tipe kendaraan]
harga_kendaraan = 4000000000 
tipe_kendaraan = "Sport Car"
merk_kendaraan = "BMW"

# - Tambahkan dari list tersebut di belakang dengan value : [harga kendaraan, tipe kendaraan]
print("Tugas Nomer : 1")

print("- Tambahkan dari list tersebut di belakang dengan value : [harga kendaraan, tipe kendaraan] : -> Hasil Dibawah :")
listVariabelKendaraan.append(harga_kendaraan)  # Menambahkan harga kendaraan ke dalam list
listVariabelKendaraan.append(tipe_kendaraan)  # Menambahkan tipe kendaraan ke dalam list
print(listVariabelKendaraan)
print()

# - Tambahkan setelah jenis kendaraan dengan value [merk kendaraan]
print("- Tambahkan setelah jenis kendaraan dengan value [merk kendaraan] : -> Hasil Dibawah :")
# Menambahkan merk kendaraan setelah jenis kendaraan
# Mendapatkan indeks jenis kendaraan
indeks_jenis_kendaraan = listVariabelKendaraan.index("Mobil")
# Menambahkan merk kendaraan setelah jenis kendaraan
listVariabelKendaraan.insert(indeks_jenis_kendaraan + 1, merk_kendaraan)
# Menampilkan list kendaraan setelah penambahan nilai
# print("List Kendaraan setelah penambahan nilai:")
print(listVariabelKendaraan)


# 2. Buat program python dengan match case untuk 
# mengitung luas bangun datar :
# jika pilih 1, maka menghitung luas persegi  
# jika pilih 2, maka menghitung luas lingkaran
# jika pilih 3, maka menghitung luas segitiga 
# selain pilihan di atas, maka keterangan : salah pilih angka
#Match Case - Perhitungan Luas - Luas Persegi, Luas Lingkaran, Luas Segitiga
# =============================================================

# 2. Buat program python dengan match case untuk 
# mengitung luas bangun datar :
penampung = '''
Tugas Nomer : 2
Selamat Datang di Program Perhitungan Menghitung Luas Bangun Datar Sederhana - Eko M H_TI02 
Syarat Menggunakan - Masukan Pilihan Perhitungan Telebih Dahulu!!  :

1. Luas Persegi
2. Luas Lingkaran
3. Luas Segitiga

Masukkan pilihan (1/2/3):  '''

pilihan = input(penampung)

#Match Case - Perhitungan Luas - Luas Persegi, Luas Lingkaran, Luas Segitiga
match pilihan:
    # jika pilih 1, maka menghitung Luas Persegi  
    #  Diketahui Rumus Persegi : L = sisi x sisi.
    case "1":
        print ("Kamu Memilih - Perhitungan Luas Persegi : ")
        sisi = int(input("Masukan sisi?"))
        luasP = sisi * sisi
        print("Luas Persegi Yang Sisi = ", sisi, ",adalah", luasP)
        
    # jika pilih 2, maka menghitung Luas Lingkaran   
    #  Diketahui Rumus Lingkaran : L  = π x r²
    case "2":
        print ("Kamu Memilih - Perhitungan Luas Lingkaran : ")
        phi = 22/7
        jari_jari = float(input("Masukan Jari - Jari? "))
        luasLingkaran = phi * jari_jari * jari_jari
        print("Luas Lingkaran Yang Jari = ", jari_jari, ",adalah ", luasLingkaran)
    
    # jika pilih 3, maka menghitung Luas Segitiga  
    #  Diketahui Rumus Segitiga :L = 1/2 x a x t
    case "3":
        print ("Kamu Memilih - Perhitungan Luas Segitiga : ")
        alas = float(input("Masukan Alas? "))
        tinggi = float(input("Masukan Tinggi? "))
        luasSegitiga = 1/2 * alas * tinggi
        print("Luas Segitiga Yang Alas = ", alas, " dan Tinggi ", tinggi, ",adalah ", luasSegitiga)
     
    # selain pilihan di atas, maka keterangan : salah pilih angka   
    case _:
        print ("Pilih Pilihan Sesuai Dengan Pilihan Yang Ada !! : ")
        
        
#  Tugas Punya : Eko Muchamad Haryono
#  TI - 02
#  Teknik Informatika
#  Dasar - Dasar Pemograman (DDP)
#  Tema : Kerjakan Soal Pertemuan - 5, Menggunakan Python


