#  Tugas Punya : Eko Muchamad Haryono
#  NIM : 0110223079
#  TI - 02
#  Teknik Informatika
#  Dasar - Dasar Pemograman (DDP)
#  Tema : Kerjakan Soal Tugas Pertemuan - 11

import math

def tambah(a, b):
    return a + b

def kurang(a, b):
    return a - b

def kali(a, b):
    return a * b

def bagi(a, b):
    if b == 0:
        return "Error: Pembagian oleh nol tidak diperbolehkan."
    else:
        return a / b

def eksponensial(a, b):
    return a ** b

def akar_kuadrat(a):
    if a < 0:
        return "Error: Akar kuadrat dari angka negatif tidak didefinisikan."
    else:
        return math.sqrt(a)

def modulus(a, b):
    if b == 0:
        return "Error: Modulus dengan pembagi nol tidak diperbolehkan."
    else:
        return a % b

def pembagian_bulat(a, b):
    if b == 0:
        return "Error: Pembagian bulat dengan pembagi nol tidak diperbolehkan."
    else:
        return a // b

def pangkat(a, b):
    return math.pow(a, b)

def logaritma(a, b):
    if a <= 0 or b <= 1:
        return "Error: Logaritma dengan basis kurang dari atau sama dengan nol, atau logaritma dari angka yang kurang dari dua tidak didefinisikan."
    else:
        return math.log(a, b)

def faktorial(a):
    if a < 0:
        return "Error: Faktorial dari angka negatif tidak didefinisikan."
    else:
        return math.factorial(a)

def permutasi(a, b):
    if a < 0 or b < 0 or a < b:
        return "Error: Permutasi dari angka negatif atau n yang lebih kecil dari r tidak didefinisikan."
    else:
        return math.perm(a, b)
    
#  Tugas Punya : Eko Muchamad Haryono
#  NIM : 0110223079
#  TI - 02
#  Teknik Informatika
#  Dasar - Dasar Pemograman (DDP)
#  Tema : Kerjakan Soal Tugas Pertemuan - 11