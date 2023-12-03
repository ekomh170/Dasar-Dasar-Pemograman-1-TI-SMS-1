#  Tugas Punya : Eko Muchamad Haryono
#  TI - 02
#  Teknik Informatika
#  Dasar - Dasar Pemograman (DDP)
#  Tema : Kerjakan Soal Tugas Pertemuan - 10

# Tugas dari file PPT Halaman 19 - 20 - Tugas Pertemuan 10 :

# 1. Nama Siswa Yang Lulus
# Buat fungsi untuk menampilkan nama2 siswa yang lulus saja dari hasil_akhir di slide sebelumnya (nilai > 65) hasil_akhir = [ 
# {'nama':'Reza', 'nilai':70}, 
# {'nama':'Ciut', 'nilai':63}, 
# {'nama':'Dian', 'nilai':80},
# {'nama':'Badu', 'nilai':40} ] 
# lulus_saja(hasil_akhir) 
# hasilnya:[‘Reza’, ‘Dian’]

def lulus_saja(hasil_akhir):
    siswa_lulus = [siswa['nama'] for siswa in hasil_akhir if siswa['nilai'] > 65]
    return siswa_lulus

hasil_akhir = [
    {'nama': 'Reza', 'nilai': 70},
    {'nama': 'Ciut', 'nilai': 63},
    {'nama': 'Dian', 'nilai': 80},
    {'nama': 'Badu', 'nilai': 40}
]

hasil_lulus = lulus_saja(hasil_akhir)
print("1.", hasil_lulus)



# 2. Membalik nama buah
# Buat fungsi untuk membuat list baru berisi urutan terbalik dari buah2an menggunakan for dan materi yang sudah diajarkan.
# (tidak boleh pakai fungsi dari python).
# balikan(['pepaya', 'mangga', 'pisang', 'durian', 'jambu']) hasilnya :['jambu', 'durian', 'pisang', 'mangga', 'pepaya']

def balikan(list_buah):
    buah_terbalik = []
    for i in range(len(list_buah) - 1, -1, -1):
        buah_terbalik.append(list_buah[i])
    return buah_terbalik

buah2an = ['pepaya', 'mangga', 'pisang', 'durian', 'jambu']
buah_terbalik = balikan(buah2an)
print("2.", buah_terbalik)



# 3. Duplikasi Nama Buah
# Buat fungsi untuk membuat list baru berisi isi list buah2an tetapi terduplikasi.
# duplikasi(['pepaya', 'mangga', 'pisang', 'durian', 'jambu'])  Hasilnya: ['pepaya', 'pepaya', 'mangga', 'mangga', 'pisang', 'pisang', 'durian', 'durian', 'jambu', 'jambu']

def duplikasi(list_buah):
    buah_terduplikasi = []
    for buah in list_buah:
        buah_terduplikasi.append(buah)
        buah_terduplikasi.append(buah)
    return buah_terduplikasi

buah2an = ['pepaya', 'mangga', 'pisang', 'durian', 'jambu']
buah_terduplikasi = duplikasi(buah2an)
print("3.", buah_terduplikasi)



# 4. Hanya Konsonan
# Buat fungsi untuk membuat string baru berisi hanya konsonan dari string 
# fungsi(“Nurul Fikri”) Hasilnya: "NrlFkr"

def hanya_konsonan(kalimat):
    konsonan = ""
    for karakter in kalimat:
        if karakter.isalpha() and karakter.lower() not in "aeiou":
            konsonan += karakter
    return konsonan

kalimat_input = "Nurul Fikri"
hasil_konsonan = hanya_konsonan(kalimat_input)
print("4.", hasil_konsonan)


# Quiz :
# Slicing, formatnya adalah [awal:akhir] 
# Ada juga [awal:akhir:step] 
# buah2an[0:5:2] # ['pepaya','pisang','jambu'] 
# ● Quiz. Coba lakukan berikut. Jelaskan mengapa begitu:

# 1. nama[4:] = nama[4:]: Ini berarti kita mengambil potongan (slice) dari string nama mulai dari indeks ke-4 hingga akhir. Jadi, kita akan mendapatkan karakter mulai dari indeks ke-4 sampai akhir dari string nama.

# 2. buah2an[1:4:2] = Ini berarti kita mengambil potongan (slice) dari list buah2an mulai dari indeks ke-1 hingga indeks ke-4 dengan langkah 2. Jadi, kita akan mendapatkan elemen pada indeks ke-1 dan indeks ke-3 dari list buah2an.

# 3. nama[::2] = Ini berarti kita mengambil potongan (slice) dari string nama mulai dari awal hingga akhir dengan langkah 2. Jadi, kita akan mendapatkan setiap karakter pada indeks genap dari string nama.

# 4. buah2an[::3] = Ini berarti kita mengambil potongan (slice) dari list buah2an mulai dari awal hingga akhir dengan langkah 3. Jadi, kita akan mendapatkan setiap elemen pada indeks yang merupakan kelipatan 3 dari list buah2an.




#  Tugas Punya : Eko Muchamad Haryono
#  TI - 02
#  Teknik Informatika
#  Dasar - Dasar Pemograman (DDP)
#  Tema : Kerjakan Soal Tugas Pertemuan - 10