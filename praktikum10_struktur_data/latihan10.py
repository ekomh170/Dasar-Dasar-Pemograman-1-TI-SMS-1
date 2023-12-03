
# Struktur Data
# Data dasar yang tersedia (bilangan, tulisan, logika) sering tidak cukup 
# ● Harus bekerja dengan data yang lebih kompleks 
# ● Struktur data:
#     – Array
#     – List
#     – Stack
#     – Queue
#     – Set
#     – Dictionary (Map)

# Array
# Berisi sekumpulan data dengan urutan tertentu, bisa ada duplikasi 
# ● Diakses dengan indeks 
# ● List di python merupakan implementasi dari array 
nilai = [65, 60, 75, 0, 98] 
nilai[0] == 65 
# True 
nilai[len(nilai)-1] == 98 
# # berarti indeks terakhir

# Stack
# ● Last In First Out. Memiliki 2 operasi:
#     – push untuk menyimpan data ke “atas” tumpukan
#     – pop untuk mengambil data yang paling “atas”
#     – https://www.programiz.com/dsa/stack

# Stack (2)
# ● list di python juga mendukung operasi stack
#     – append untuk push
#     – pop 

bilangan = [1,2,3] 
a = bilangan.pop() 
bilangan.append(6) 
print(bilangan) # => [1,2,6] 
print(a) # => 3

# Stack (3), kegunaan
# ● Pengecekan tanda kurung
    #   - (a+b) * (c[d + e) 
# ● Pencatatan undo dan redo


data_diri = { "nama":"Reza", "matpel":"DDP"} 
data_diri['nama']="Dian";

print(data_diri['nama'])