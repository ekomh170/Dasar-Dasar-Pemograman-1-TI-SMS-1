#  Tugas Punya : Eko Muchamad Haryono
#  NIM : 0110223079
#  TI - 02
#  Teknik Informatika (TI)
#  Dasar - Dasar Pemograman (DDP)
#  Tema : Kerjakan Soal Tugas Pertemuan - 13

from animals_superclass import *

# SubClass / Child classes
class Ikan(Animal):
    usia=""
    kondisi=""
    
    def __init__(self, nama, makanan, tempat_hidup, berkembang_biak, usia, kondisi):
        super().__init__(nama, makanan, tempat_hidup, berkembang_biak)
        self.usia = usia
        self.kondisi = kondisi

    def cetak_info(self):
        super().cetak_info()
        print(f"Usia \t\t: {self.usia}",
              f"\nKondisi \t: {self.kondisi}",
              "\n-------------------------------")
        
#  Tugas Punya : Eko Muchamad Haryono
#  NIM : 0110223079
#  TI - 02
#  Teknik Informatika (TI)
#  Dasar - Dasar Pemograman (DDP)
#  Tema : Kerjakan Soal Tugas Pertemuan - 13