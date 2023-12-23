#  Tugas Punya : Eko Muchamad Haryono
#  NIM : 0110223079
#  TI - 02
#  Teknik Informatika (TI)
#  Dasar - Dasar Pemograman (DDP)
#  Tema : Kerjakan Soal Tugas Pertemuan - 13

# Parent class / SuperClass
class Animal:
    nama = ""
    makanan = ""
    tempat_hidup = ""
    berkembang_biak = ""
    
    def __init__(self, nama, makanan, tempat_hidup, berkembang_biak):
        self.nama = nama
        self.makanan = makanan
        self.tempat_hidup = tempat_hidup
        self.berkembang_biak = berkembang_biak

    def cetak_info(self):
        print(f"\n\033[1mPenjelasan Masing - Masing Hewan :\n\033[0m",
              f"\n\033[91mNama \t\t: {self.nama}\033[0m",
              f"\nMakanan \t: {self.makanan}",
              f"\nTempat Hidup \t: {self.tempat_hidup}",
              f"\nBerkembang Biak : {self.berkembang_biak}",
              "\n-------------------------------")
        
#  Tugas Punya : Eko Muchamad Haryono
#  NIM : 0110223079
#  TI - 02
#  Teknik Informatika (TI)
#  Dasar - Dasar Pemograman (DDP)
#  Tema : Kerjakan Soal Tugas Pertemuan - 13
