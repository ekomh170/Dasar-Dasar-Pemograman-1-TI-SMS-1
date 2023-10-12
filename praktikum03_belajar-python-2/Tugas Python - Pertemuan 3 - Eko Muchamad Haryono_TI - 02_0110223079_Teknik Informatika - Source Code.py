
# Soal

print("")
print("")
print("Tugas Pertemuan dan Praktikum 3 - DDP")
print("")
print("")

# 1. Buatlah program python untuk menuliskan profil pribadi (nama, nim, kelas, no telp, alamat) menggunakan variabel dan di cetak (print)

nm = "Eko Muchamad Haryono,"
nim = "0110223079,"
kls = "TI-02,"
no = "082246105463,"
almt = "Citeureup"

print("1. Profil Pribadi :", nm, nim, kls, no, almt)

print("")
print("")
# 2. buat seperti no 1 tapi 1 nama teman kalian 
nm = "Yossy Indra Kusuma,"
nim = "0110223073,"
kls = "TI-02,"
no = "081211462862,"
almt = "Bojong Gede"

print("2. Profil Teman :", nm, nim, kls, no, almt)

print("")
print("")
# 3. buat program python untuk mencari nilai berat badan ideal 


gender = str(input("Pilih Gender 'pria atau wanita' Untuk Mencari Berat Badan Ideal : "))

if "pria" == gender . lower() or "wanita" == gender . lower():
    print ("Mendeteksi Berat Badan Yang Di Pilih = " + gender)
    
else:  
    print ("Masukan Berat Badan Dahulu Jika Tidak Program Penghitungan Berat Badan Tidak Berjalan !! ")
    gender = str(input("Pilih Gender 'pria atau wanita' Untuk Mencari Berat Badan Ideal : "))
    print ("Mendeteksi Berat Badan Yang Di Pilih = " + gender)
   
tinggi_badan = int(input("3.1. Masukan Tinggi  Badan  :"))
if  "pria" == gender . lower():
# Tujuan Berat badan ideal (kilogram) 
# Pria = (tinggi badan  – 100) – (tinggi badan  – 100) x 10 persen]
    pria_berat_badan_ideal_kg = (tinggi_badan - 100) - (tinggi_badan - 100) * 10/100
    print("3.3 Berat Badan Ideal Pria :", pria_berat_badan_ideal_kg)
# Wanita = (tinggi badan  – 100) – (tinggi badan  – 100) x 15 persen]
    if "wanita" == gender . lower():
        wanita_berat_badan_ideal_kg = (tinggi_badan - 100) - (tinggi_badan - 100) * 15/100
        print("3.3. Berat Badan Ideal Wanita :", wanita_berat_badan_ideal_kg)
    
    print("")
    print("")
    # 4. buat program python untuk mencari nilai konversi dari Celcius ke Fahrenheit 
    # Konversi Nilai Celcius To Fahrenheit
    celcius = float(input("4.1. Masukan Nilai Celcius  :"))
    fahrenheit = (9/5) * celcius + 32
    print("4.1. Nilai Dalam Konversi Celcius Ke -> Fahrenheit :", fahrenheit, "F")

    # Konversi Nilai Fahrenheit  To Celcius

    fahrenheit = float(input("4.2. Masukan Nilai Fahrenheit  :"))
    celcius = (fahrenheit-32) * 5/9
    print("4.2. Nilai Dalam Konversi Fahrenheit Ke -> Celcius :", celcius, "C")


    print("")
    print("")
    # 5. buat program python untuk mencari luas dan keliling tabung.

    # Keliling Tabung
    # 2 * 3,14 * R
    # K = 2πr

    tinggi = float(input("5.1 Masukan - Tinggi Tabung :"))
    jari_jari = float(input("5.2 Masukan - Jari - Jari Tabung :"))

    k_tabung = 2 * 22/7 * jari_jari
    print("5.1. Hasil Tabung Keliling : ", k_tabung)

    # Luas Tabung
    # L = 2 * 22/7 * R * (R+T)
    l_tabung = 2 * 22/7 * jari_jari * (jari_jari + tinggi)
    print("5.2. Hasil Tabung Luas :", l_tabung)
    print("")
    print("")