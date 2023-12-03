# Hasil Links PDF : https://github.com/ekomh170/Dasar-Dasar-Pemograman-1-TI-SMS-1/blob/ry_dev/uts/UTS_Eko%20Muchamad%20Haryono%20Haryono_TI02_0110223079.pdf

print("")
# 1. Apa yang di maksud dengan variabel dalam Bahasa pemprograman python? Dan berikan contoh pendeklarasian variabel yang benar dan salah (bobot 10) (CPMK01)
#  Jawaban DDP Soal Nomer 1 :
# Dalam pemrograman Python, variabel adalah tempat penyimpanan yang
# digunakan untuk menampung nilai atau data. Setiap variabel memiliki tipe data
# tertentu, seperti integer (bilangan bulat), float (bilangan desimal), string (teks),
# dan lain sebagainya.

# Contoh Dari Pendeklarasi Variabel
# Saya Mendeklarasikan variable nama (tipe data : string), umur (tipe data : interger), kampus (tipe data :string) 

nama = "Eko Muchamad Haryono";
umur = 20;
kampus = "Sekolah Tinggi Teknologi Terpadu Nurul Fikri"

# Print Di Gunakan Untuk Menampilkan Variabel -> Karena Variabel Yang Di Simpan Juga Dapat Di Panggil
print("Perkenalkan Saya ",nama, "Saya Berkuliah ",kampus , "Saya Berumur", umur, "\n")

# ################################################################################################

# 2. Sebutkan dan jelaskan tipe data yang ada di Bahasa Pemprograman Python, minimal 4! (bobot 10) (CPMK01) :
# Di Bahasa Pemograman Python, tipe data mengacu pada karakteristik nilai
# yang dapat disimpan dan dioperasikan oleh variabel atau objek dalam
# program.Tipe Data Yang Ada Di Python dan Syantax Cara Mengecek Tipe
# Data Variabel Di Python :

# Integer (int):    
# Tipe data ini merepresentasikan bilangan bulat.
# Contoh: 
tahun_lahir = 2003;
print(tahun_lahir, "= Jenis Tipe Data :", type(tahun_lahir))

# Float (float):
# Tipe data ini merepresentasikan bilangan desimal atau floating-point.
# Contoh: 
nilai_ipk = 3.99
print(nilai_ipk, "= Jenis Tipe Data :", type(nilai_ipk))

# String (str):
# Tipe data ini merepresentasikan teks atau karakter.
# Contoh: 
nama = "Eko Muchamad Haryono"
print(nama, "= Jenis Tipe Data :", type(nama))

# Boolean (bool):
# Tipe data ini merepresentasikan nilai kebenaran, yaitu True atau False.
# Contoh: 
kondisi = 7 > 8
print(kondisi, "= Jenis Tipe Data :", type(kondisi))

# ################################################################################################

# 3. Buatlah Sebuah Flowchart untuk:
# Jika NIM ganjil : menstransfer uang melalui mobile banking
# Links Flowchat : https://github.com/ekomh170/Dasar-Dasar-Pemograman-1-TI-SMS-1/blob/ry_dev/uts/Flowchart%20Soal%20Nomer%203%20DDP%20UTS%20-%20Eko.vsdx
# Links PDF : https://github.com/ekomh170/Dasar-Dasar-Pemograman-1-TI-SMS-1/blob/ry_dev/uts/UTS_Eko%20Muchamad%20Haryono%20Haryono_TI02_0110223079.pdf

# ################################################################################################

# 4. Buatlah sebuah pseudo code dan Program dengan bahasa pemprograman python untuk menghitung luas dan keliling :
# Jika NIM ganjil : layang - layang
#  (bobot 25) (CPMK02)

# Pseudocode :
# 1. Input panjang diagonal 1 (d1)
# 2. Input panjang diagonal 2 (d2)
# 3. Hitung luas layang-layang (L) dengan rumus: L = (1/2) * d1 * d2
# 4. Hitung keliling layang-layang (K) dengan rumus: K = 2 * (sisi1 + sisi2), di mana sisi1 dan sisi2 adalah panjang sisi-sisi layang-layang
# 5. Tampilkan hasil luas dan keliling layang-layang

# implementasi program Python berdasarkan pseudocode
d1 = float(input("Masukkan panjang diagonal 1: "))
d2 = float(input("Masukkan panjang diagonal 2: "))

luas = 0.5 * d1 * d2

sisi1 = (d1**2 + d2**2)**0.5 / 2
sisi2 = sisi1

keliling = 2 * (sisi1 + sisi2)

print(f"Luas layang-layang: {luas}")
print(f"Keliling layang-layang: {keliling}", "\n")

# ################################################################################################

# 5. Buatlah sebuah Program Untuk membuat kalkulator sederhana dengan  Bahasa Python dengan ketentuan sebagai berikut ? (Bobot 40) (CPMK02)

# Inputan : 
# Masukan angka 1 : 
# Masukan angka 2 : 

# Pilih operator : 

# Operator keterangan
# + Tambah
# - Kurang
# / Bagi
# Kali
# Pangkat

# Program Kalkulator Sederhana

print("Selamat Datang Di Kalkulator Sederhana - Eko Muchamad Haryono")

angka1 = float(input("Masukkan angka 1 : "))
angka2 = float(input("Masukkan angka 2 : "))

print("\nPilih Operator:")
print("+ Tambah")
print("- Kurang")
print("/ Bagi")
print("* Kali")
print("^ Pangkat")

operator = input("Masukkan operator: ")

if operator == '+':
    hasil = angka1 + angka2
    print(f"Hasil: {angka1} + {angka2} = {hasil}")
elif operator == '-':
    hasil = angka1 - angka2
    print(f"Hasil: {angka1} - {angka2} = {hasil}")
elif operator == '/':
    if angka2 != 0:
        hasil = angka1 / angka2
        print(f"Hasil: {angka1} / {angka2} = {hasil}")
    else:
        print("Error! Pembagian dengan angka 0 tidak diperbolehkan.")
elif operator == '*':
    hasil = angka1 * angka2
    print(f"Hasil: {angka1} * {angka2} = {hasil}")
elif operator == '^':
    hasil = angka1 ** angka2
    print(f"Hasil: {angka1} ^ {angka2} = {hasil}")
else:
    print("Operator tidak valid. Silakan pilih operator yang sesuai.")