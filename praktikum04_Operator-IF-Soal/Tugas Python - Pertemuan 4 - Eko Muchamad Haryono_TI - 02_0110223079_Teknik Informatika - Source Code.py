print("")
print("")
# 1. buatlah sebuah program python yang menghasilkan nilai dari perbandingan 2 variabel

# Meminta pengguna memasukkan dua variabel
variabel_pertama = input("1.1. Masukkan variabel pertama : ")
variabel_kedua = input("1.1. Masukkan variabel kedua : ")

# Membandingkan dua variabel dan menampilkan hasilnya
if variabel_pertama == variabel_kedua:
    print("Variabel " + variabel_pertama +" sama dengan Variabel " + variabel_kedua)
else:
    print("Variabel " + variabel_pertama + " tidak sama dengan Variabel " + variabel_kedua)


print("")
print("")
# 2. buat program python menggunakan if, elif dan else untuk konversi suhu

# Konversi Suhu

# Konversi Nilai Celcius To Fahrenheit
print("2.0. Pilih Konversi Suhu -> Konversi Celcius Ke -> Fahrenheit")
print("1. Celcius Konversi Fahrenheit")
print("2. Fahrenheit Konversi Celcius")
print("")

pilihan = input("2.1. Masukkan nomor operasi (1/2): ")

if pilihan == '1':
    # Konversi Nilai Celcius To Fahrenheit
    celcius = float(input("2.1. Masukan Nilai Celcius  : "))
    fahrenheit = (9/5) * celcius + 32
    print("2.1. Nilai Dalam Konversi Celcius Ke -> Fahrenheit :", fahrenheit, "F")
elif pilihan == '2':
# Konversi Nilai Fahrenheit  To Celcius
    fahrenheit = float(input("2.2. Masukan Nilai Fahrenheit  : "))
    celcius = (fahrenheit-32) * 5/9
    print("2.1. Nilai Dalam Konversi Fahrenheit Ke -> Celcius :", celcius, "C")
# Konversi Suhu


# if, elif dan else
if (celcius < 15) :
    print("2.3. Berdasarkan Pengecekan Suhu Yang Di Inputkan Kondisi Suhu Saat Ini Adalah, Sangat Dingin")
elif(celcius < 25) :
    print("2.3. Berdasarkan Pengecekan Suhu Yang Di Inputkan Kondisi Suhu Saat Ini Adalah, Dingin")
elif(celcius < 36) :
    print("2.3. Berdasarkan Pengecekan Suhu Yang Di Inputkan Kondisi Suhu Saat Ini Adalah, Normal")
elif(celcius < 46) :
    print("2.3. Berdasarkan Pengecekan Suhu Yang Di Inputkan Kondisi Suhu Saat Ini Adalah, Panas") 
elif(celcius < 60 or celcius > 60) :
    print("2.3. Berdasarkan Pengecekan Suhu Yang Di Inputkan Kondisi Suhu Saat Ini Adalah, Sangat Panas")
else :
    print("Isi Suhu Dahulu !!")
    
print("")
print("")
# 3. buat program python untuk menampilkan status mahasiswa berdasarkan keaktifkannya
# Kehadiran Mahasiswa

# Jumlah Pertemuan Mahasiswa
nama_mahasiswa = str(input("3.1. Masukan Nama Mahasiswa : "))
ket_mahasiswa = ", Adalah Mahasiswa Yang Memiliki "

total_pertemuan_mahasiswa =  int(input("3.2. Masukan Total Pertemuan : ")) 
jumlah_kehadiran_mahasiswa = int(input("3.3. Masukan Total Kehadiran Mashasiswa : "))

# Rumus Kehadiran Mahasiswa = Jumlah Kehadiran Mahasiswa : Jumlah Pertemuan * 100%
hasil_kehadiran_mhs = jumlah_kehadiran_mahasiswa / total_pertemuan_mahasiswa  * 100/1

print("3.4. Hasil Total Nilai Mahasiswa : ", hasil_kehadiran_mhs)

if(hasil_kehadiran_mhs < 40) :
    print("3.5. " + nama_mahasiswa + ket_mahasiswa + "Nilai Kehadiran : E")
elif(hasil_kehadiran_mhs < 50) :
     print("3.5. " + nama_mahasiswa + ket_mahasiswa + "Nilai Kehadiran : D")
elif(hasil_kehadiran_mhs < 70) : 
    print("3.5. " + nama_mahasiswa + ket_mahasiswa + "Nilai Kehadiran : C")
elif(hasil_kehadiran_mhs < 80) : 
    print("3.5. " + nama_mahasiswa + ket_mahasiswa + "Nilai Kehadiran : B")    
elif(hasil_kehadiran_mhs < 100) : 
    print("3.5. " + nama_mahasiswa + ket_mahasiswa + "Nilai Kehadiran : A")
else :
    print("Isi Nilai Dahulu !!")
# Jumlah Kehadiran Mahasiswa

print("")
print("")
# 4. buat program kalkulator sederhana

# Definisikan fungsi kalkulator
def tambah(x, y):
    return x + y

def kurang(x, y):
    return x - y

def kali(x, y):
    return x * y

def bagi(x, y):
    if y == 0:
        return "Error! Pembagian dengan nol tidak diizinkan."
    return x / y

# Tampilkan menu operasi
print("5.0. Pilih operasi Kalkulator Sederhana :")
print("1. Penjumlahan")
print("2. Pengurangan")
print("3. Perkalian")
print("4. Pembagian")
print("")

# Input dari pengguna
pilihan = input("5.1. Masukkan nomor operasi (1/2/3/4): ")

angka1 = float(input("5.1. Masukkan angka pertama : "))
angka2 = float(input("5.1. Masukkan angka kedua: "))

# Tentukan operasi berdasarkan pilihan pengguna
if pilihan == '1':
    print("5.2. Hasil: ", tambah(angka1, angka2))
elif pilihan == '2':
    print("5.2. Hasil: ", kurang(angka1, angka2))
elif pilihan == '3':
    print("5.2. Hasil: ", kali(angka1, angka2))
elif pilihan == '4':
    print("5.2. Hasil: Dari Kalkulator Sederhana Adalah : ", bagi(angka1, angka2))
else:
    print("Pilihan operasi tidak valid.")

# 5. untuk hasilnya di kumpulkan ke email : ridhobigboy@gmail.com

# 6. maximal pengumpulan malam ini jam  01.00