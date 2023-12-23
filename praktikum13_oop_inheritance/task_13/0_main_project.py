#  Tugas Punya : Eko Muchamad Haryono
#  NIM : 0110223079
#  TI - 02
#  Teknik Informatika (TI)
#  Dasar - Dasar Pemograman (DDP)
#  Tema : Kerjakan Soal Tugas Pertemuan - 13

from badak_subclass_1 import *
from ikan_subclass_2 import *
from ular_subclass_3 import *

# Menciptakan Object Dari Setiap Kelas
badak = Badak("Badak Bercula Satu", "Tanaman", "Hutan Tropis", "Vivipar", "10 kilogram", "Abu - Abu")
hiu_putih = Ikan("Hiu Putih", "Ikan & Mamalia Laut", "Lautan", "Ovovivipar", "20 Tahun", "Terluka")
ular_kobra = Ular("Ular Kobra", "Ular Kecil, Kelinci & Burung Kecil", "Hutan Lebat", "Vivipar", "2 Meter", True)

# Memanggil method cetak_info dari setiap objek
badak.cetak_info()
hiu_putih.cetak_info()
ular_kobra.cetak_info()

#  Tugas Punya : Eko Muchamad Haryono
#  NIM : 0110223079
#  TI - 02
#  Teknik Informatika (TI)
#  Dasar - Dasar Pemograman (DDP)
#  Tema : Kerjakan Soal Tugas Pertemuan - 13