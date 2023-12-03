#  Tugas Punya : Eko Muchamad Haryono
#  TI - 02
#  Teknik Informatika
#  Dasar - Dasar Pemograman (DDP)
#  Tema : Kerjakan Soal Pertemuan - 8, Menggunakan Python --> Materi Python Function

# Soal =====================================================
# 1. buatlah fungsi untuk menampilakan data diri :
# contoh pemanggilan : profil(nama, alamat, gender, umur, hoby)

# deklarasi fungsi 
def profile(nama, alamat,gender, umur, hoby):
        print("\n1. Pemanggilan Fungsi Profile = Run Program =",nama, alamat, gender, umur, hoby, "\n")

# pemanggilan fungsi
profile("Eko", "Citeureup", "Laki - Laki", 20, "Membuat Program Dengan Bahasa Pemograman Python");

# Soal =====================================================
# 2. buatlah fungsi untuk mencari kelulusan nilai dari berikut : 
# jika nilai < 60 maka gagal 
# jika nilai = 61 - 70 maka baik 
# jika nilai = 71 - 80 maka sangat baik 
# jika nilai = 81 - 100 maka istimewa 
# ex:
# nilai (60)

# deklarasi fungsi 
def cek_kelulusan(nilai):
    ket = "2. Hasil Cek Fungsi -> Kelulusan = Run Program ="
    if nilai <= 60:
        print(ket,"Gagal\n")
    elif nilai >= 61 and nilai <= 70:
        print(ket,"Baik\n")
    elif nilai >= 71 and nilai <= 80:
        print(ket,"Sangat Baik\n")
    elif nilai >= 81 and nilai <= 100:
       print(ket,"Istimewa\n")
    else:
        print(ket, "Nilai tidak valid\n")

# pemanggilan fungsi
cek_kelulusan(60);

# Soal =====================================================
# 3. buatlah fungsi untuk mencetak nilai bilangan ganjil dari parameter yang di masukan :
# ex : ganjil (100)

print("3. Hasil Jawaban Nomer 3 Mencetak Bilangan Ganjil Menggunakan Fungsi :\n")

# deklarasi fungsi 
def ganjil(n):
    ganjil_list = [i for i in range(1, n+1, 2)]
    print(ganjil_list, "\n")

# pemanggilan fungsi
ganjil(100)

#  Tugas Punya : Eko Muchamad Haryono
#  TI - 02
#  Teknik Informatika
#  Dasar - Dasar Pemograman (DDP)
#  Tema : Kerjakan Soal Pertemuan - 8, Menggunakan Python --> Materi Python Function