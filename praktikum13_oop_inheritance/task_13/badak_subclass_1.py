#  Tugas Punya : Eko Muchamad Haryono
#  NIM : 0110223079
#  TI - 02
#  Teknik Informatika (TI)
#  Dasar - Dasar Pemograman (DDP)
#  Tema : Kerjakan Soal Tugas Pertemuan - 13

from animals_superclass import *

# SubClass / Child classes
class Badak(Animal):
    berat_cula = ""
    warna_kulit = ""
    
    def __init__(self, nama, makanan, tempat_hidup, berkembang_biak, berat_cula, warna_kulit):
        super().__init__(nama, makanan, tempat_hidup, berkembang_biak)
        self.berat_cula = berat_cula
        self.warna_kulit = warna_kulit

    def cetak_info(self):
        super().cetak_info()
        print(f"Berat Cula \t: {self.berat_cula}",
              f"\nWarna Kulit \t: {self.warna_kulit}",
              "\n-------------------------------")
        
#  Tugas Punya : Eko Muchamad Haryono
#  NIM : 0110223079
#  TI - 02
#  Teknik Informatika (TI)
#  Dasar - Dasar Pemograman (DDP)
#  Tema : Kerjakan Soal Tugas Pertemuan - 13        