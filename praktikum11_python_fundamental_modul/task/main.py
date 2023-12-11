#  Tugas Punya : Eko Muchamad Haryono
#  NIM : 0110223079
#  TI - 02
#  Teknik Informatika
#  Dasar - Dasar Pemograman (DDP)
#  Tema : Kerjakan Soal Tugas Pertemuan - 11

# 1. Buat Module - Bangun Datar (Minimal 7)
# - Persegi = 1
# - Persegi Panjang = 2
# - Lingkaran = 3
# - Segitiga = 4
# - Belah Ketupat = 5
# - Layang - Layang = 6
# - Trapesium = 7
# - Jajar Genjang = 8

from bangun_datar_modul import *
# isi dari import * = luas_persegi, luas_persegi_panjang, luas_lingkaran, luas_segitiga, luas_belah_ketupat, luas_layang_layang, luas_trapesium, luas_jajar_genjang, keliling_persegi, keliling_persegi_panjang, keliling_lingkaran, keliling_segitiga, keliling_belah_ketupat, keliling_layang_layang, keliling_trapesium, keliling_jajar_genjang, 

from aritmatika_modul import *
# isi dari import * = tambah, kurang, kali, bagi, eksponensial, akar_kuadrat, modulus, pembagian_bulat, pangkat, logaritma, faktorial, permutasi

def bangun_datar():
    print("\nSelamat Datang di Aplikasi Python Penghitungan Sederhana\nBangun Datar & Aritmatika Sederhana - Milik Eko Muchamad Haryono")
    print("\nPilih bangun datar yang ingin ditampilkan:")
    print("1. Persegi")
    print("2. Persegi Panjang")
    print("3. Lingkaran")
    print("4. Segitiga")
    print("5. Belah Ketupat")
    print("6. Layang-Layang")
    print("7. Trapesium")
    print("8. Jajar Genjang")

    pilihan = int(input("\nMasukkan Nomor Bangun Datar yang dipilih (1-8):"))

    if pilihan == 1:
        sisi = float(input("Masukkan panjang sisi persegi: "))
        print("1. luas Persegi:", luas_persegi(sisi))
        print("2. Keliling Persegi:", keliling_persegi(sisi))
    elif pilihan == 2:
        panjang = float(input("Masukkan panjang persegi panjang: "))
        lebar = float(input("Masukkan lebar persegi panjang: "))
        print("1. Luas Persegi Panjang:", luas_persegi_panjang(panjang, lebar))
        print("2. Keliling Persegi Panjang:", keliling_persegi_panjang(panjang, lebar))
    elif pilihan == 3:
        jari_jari = float(input("Masukkan panjang jari-jari lingkaran: "))
        print("1. Luas Lingkaran:", luas_lingkaran(jari_jari))
        print("2. Keliling Lingkaran:", keliling_lingkaran(jari_jari))
    elif pilihan == 4:
        alas = float(input("Masukkan panjang alas segitiga: "))
        tinggi = float(input("Masukkan tinggi segitiga: "))
        print("1. Hasil Luas Segitiga:", luas_segitiga(alas, tinggi))
        # Untuk segitiga, keliling bisa dihitung dengan menjumlahkan panjang sisi-sisinya
        sisi1 = float(input("\nMasukkan panjang sisi pertama segitiga: "))
        sisi2 = float(input("Masukkan panjang sisi kedua segitiga: "))
        sisi3 = float(input("Masukkan panjang sisi ketiga segitiga: "))
        print("2. Hasil Keliling Segitiga:", keliling_segitiga(sisi1, sisi2, sisi3))
    elif pilihan == 5:
        diagonal1 = float(input("Masukkan panjang diagonal 1 belah ketupat: "))
        diagonal2 = float(input("Masukkan panjang diagonal 2 belah ketupat: "))
        print("1. Luas Belah Ketupat:", luas_belah_ketupat(diagonal1, diagonal2))
        print("2. Keliling Belah Ketupat:", keliling_belah_ketupat(diagonal1))
    elif pilihan == 6:
        diagonal1 = float(input("Masukkan panjang diagonal 1 layang-layang: "))
        diagonal2 = float(input("Masukkan panjang diagonal 2 layang-layang: "))
        print("1. Luas Layang-Layang:", luas_layang_layang(diagonal1, diagonal2))
        print("2. Keliling Layang-Layang:", keliling_layang_layang(diagonal1))
    elif pilihan == 7:
        alas1 = float(input("Masukkan panjang alas trapesium: "))
        alas2 = float(input("Masukkan panjang sisi sejajar alas trapesium: "))
        tinggi = float(input("Masukkan tinggi trapesium: "))
        print("1. Luas Trapesium:", luas_trapesium(alas1, alas2, tinggi))
        # Untuk trapesium, keliling bisa dihitung dengan menjumlahkan panjang sisi-sisinya
        sisi1 = float(input("\nMasukkan panjang sisi pertama trapesium: "))
        sisi2 = float(input("Masukkan panjang sisi kedua trapesium: "))
        sisi3 = float(input("Masukkan panjang sisi ketiga trapesium: "))
        sisi4 = float(input("Masukkan panjang sisi keempat trapesium: "))
        print("2. Keliling Trapesium:", keliling_trapesium(sisi1, sisi2, sisi3, sisi4))
    elif pilihan == 8:
        alas = float(input("Masukkan panjang alas jajar genjang: "))
        tinggi = float(input("Masukkan tinggi jajar genjang: "))
        print("1. Luas Jajar Genjang:", luas_jajar_genjang(alas, tinggi))
        print("2. Keliling Jajar Genjang:", keliling_jajar_genjang(alas, alas))
    else:
        print("Pilihan tidak valid.")

if __name__ == "__main__":
    bangun_datar()



# 2. Buat Module - Hitungan Aritmatika (Minimal 10)
# Penambahan 
# Pengurangan 
# Perkalian 
# Pembagian
# Eksponensial 
# Akar Kuadrat

def hitungan_aritmatika():
    print("\nPilih operasi aritmatika yang ingin dilakukan:")
    print("1. Penambahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")
    print("5. Eksponensial")
    print("6. Akar Kuadrat")
    print("7. Modulus")
    print("8. Pembagian Bulat")
    print("9. Pangkat")
    print("10. Logaritma")
    print("11. Faktorial")
    print("12. Permutasi")

    pilihan = int(input("\nMasukkan nomor operasi aritmatika yang dipilih (1-12): "))

    if pilihan == 1:
        a = float(input("Masukkan angka pertama: "))
        b = float(input("Masukkan angka kedua: "))
        print("Hasil Penambahan:", tambah(a, b))
    elif pilihan == 2:
        a = float(input("Masukkan angka pertama: "))
        b = float(input("Masukkan angka kedua: "))
        print("Hasil Pengurangan:", kurang(a, b))
    elif pilihan == 3:
        a = float(input("Masukkan angka pertama: "))
        b = float(input("Masukkan angka kedua: "))
        print("Hasil Perkalian:", kali(a, b))
    elif pilihan == 4:
        a = float(input("Masukkan angka pembilang: "))
        b = float(input("Masukkan angka penyebut (tidak boleh nol): "))
        print("Hasil Pembagian:", bagi(a, b))
    elif pilihan == 5:
        a = float(input("Masukkan angka dasar: "))
        b = float(input("Masukkan eksponen: "))
        print("Hasil Eksponensial:", eksponensial(a, b))
    elif pilihan == 6:
        a = float(input("Masukkan angka untuk diakarkan: "))
        print("Hasil Akar Kuadrat:", akar_kuadrat(a))
    elif pilihan == 7:
        a = float(input("Masukkan angka pertama: "))
        b = float(input("Masukkan angka kedua (tidak boleh nol): "))
        print("Hasil Modulus:", modulus(a, b))
    elif pilihan == 8:
        a = float(input("Masukkan angka pembilang: "))
        b = float(input("Masukkan angka penyebut (tidak boleh nol): "))
        print("Hasil Pembagian Bulat:", pembagian_bulat(a, b))
    elif pilihan == 9:
        a = float(input("Masukkan angka dasar: "))
        b = float(input("Masukkan pangkat: "))
        print("Hasil Pangkat:", pangkat(a, b))
    elif pilihan == 10:
        a = float(input("Masukkan angka logaritma: "))
        b = float(input("Masukkan basis logaritma (harus lebih besar dari 1): "))
        print("Hasil Logaritma:", logaritma(a, b))
    elif pilihan == 11:
        a = int(input("Masukkan angka untuk dihitung faktorial: "))
        print("Hasil Faktorial:", faktorial(a))
    elif pilihan == 12:
        n = int(input("Masukkan nilai n untuk permutasi: "))
        r = int(input("Masukkan nilai r untuk permutasi: "))
        print("Hasil Permutasi:", permutasi(n, r))
    else:
        print("Pilihan tidak valid.")

if __name__ == "__main__":
    hitungan_aritmatika()

#  Tugas Punya : Eko Muchamad Haryono
#  NIM : 0110223079
#  TI - 02
#  Teknik Informatika
#  Dasar - Dasar Pemograman (DDP)
#  Tema : Kerjakan Soal Tugas Pertemuan - 11