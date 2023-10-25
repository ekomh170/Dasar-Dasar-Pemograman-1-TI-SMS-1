# Lets  Code
# Kerjakan Soal Praktikum05

# 1. - Buat variabel List Dengan Value : [namaKendaraan, JenisKendaraan, ccKendaraan. warna kendaraan, roda kendaraan]
listVariabel = ["BMW M3 GTR E46", "Mobil", "4000cc", "Biru", 4]
listBelakang = ["4000.000.000", "Sport Car"]
listSetelah = ["BMW"]

# - Tambahkan dari list tersebut di belakang dengan value : [harga kendaraan, tipe kendaraan]
print()
listVariabel.append(listBelakang)
print(listVariabel)
print()

# - Tambahkan setelah jenis kendaraan dengan value [merk kendaraan]
listVariabel.insert(2, "BMW")
print(listVariabel)
print()


# 2. Buat program python dengan match case untuk 
# mengitung luas bangun datar :
# jika pilih 1, maka menghitung luas persegi  
# jika pilih 2, maka menghitung luas lingkaran
# jika pilih 3, maka menghitung luas segitiga 
# selain pilihan di atas, maka keterangan : salah pilih angka

#Match Case - Perhitungan Luas - Luas Persegi, Luas Lingkaran, Luas Segitiga

penampung = '''

Selamat Datang di Aplikasi Perhitungan  Menghitung Luas Bangun Datar :
Masukan Pilihan Perhitungan Bangun Datar :

1. Luas Persegi
2. Luas Lingkaran
3. Luas Segitiga

Opsi Yang Di Pilih :
'''

pilihan = input(penampung)

match pilihan:
    case "1":
        print ("Kamu Memilih - Perhitungan Luas Persegi : ")
        sisi = int(input("Masukan sisi?"))
        luasP = sisi * sisi
        print("Luas Persegi Yang Sisinya ", sisi, "adalah ", luasP)
        
    case "2":
        print ("Kamu Memilih - Perhitungan Luas Lingkaran : ")
        phi = 22/7
        jari_jari = float(input("Masukan Jari - Jari? "))
        luasLingkaran = phi * jari_jari * jari_jari
        print("Luas Lingkaran Yang Jari ", jari_jari, "adalah ", luasLingkaran)
        
    case "3":
        print ("Kamu Memilih - Perhitungan Luas Segitiga : ")
        alas = float(input("Masukan Alas? "))
        tinggi = float(input("Masukan Tinggi? "))
        luasSegitiga = 1/2 * alas * tinggi
        print("Luas Segitiga Yang Alas dan Tinggi ", alas, "adalah ", luasSegitiga)
        
    case _:
        print ("Pilih Pilihan Yang Ada!!! : ")
        
        
       




