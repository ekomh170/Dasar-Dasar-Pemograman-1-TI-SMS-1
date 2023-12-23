#  Tugas Punya : Eko Muchamad Haryono
#  NIM : 0110223079
#  TI - 02
#  Teknik Informatika (TI)
#  Dasar - Dasar Pemograman (DDP)
#  Tema : Kerjakan Soal Tugas Pertemuan - 13

from animals_superclass import *

# SubClass / Child classes  
class Ular(Animal):
    panjang_ular=""
    berbisa=""
    
    def __init__(self, nama, makanan, tempat_hidup, berkembang_biak, panjang_ular, berbisa):
        super().__init__(nama, makanan, tempat_hidup, berkembang_biak)
        self.panjang_ular = panjang_ular
        self.berbisa = berbisa

    def cetak_info(self):
        super().cetak_info()
        print(f"Panjang Ular \t: {self.panjang_ular}",
              f"\nBerbisa \t: {self.berbisa}",
              "\n-------------------------------")

#  Tugas Punya : Eko Muchamad Haryono
#  NIM : 0110223079
#  TI - 02
#  Teknik Informatika (TI)
#  Dasar - Dasar Pemograman (DDP)
#  Tema : Kerjakan Soal Tugas Pertemuan - 13