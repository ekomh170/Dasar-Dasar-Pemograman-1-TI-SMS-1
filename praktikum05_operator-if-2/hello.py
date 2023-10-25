# If Condition
a = 10
b = 15
if b> a:
    print("b lebih besar dari a")
    
# Elif Condition
a = 10
b = 10
if b > a:
    print("b lebih besar dari a")
elif a == b:
    print("a sama dengan b")
    
# Else
a = 100
b = 10
if b> a:
    print("b lebih besar dari a")
elif a == b:
    print("a sama dengan b")
else:
    print("a lebih besar dari b")
    
# Short Hand If and if else

if a > b: print("a is greater than b")

# Atau

a = 2
b = 330
print("A") if a > b else print("B")

# Python List
# Syntax:

mylist = ["apple", "banana", "cherry"]

# Mengakses Element list
# Mengakses Elemen dalam List
my_list = [1, 2, 3, 4, 5]
print(my_list[0]) # Akan mencetak 1 print(my_list[3]) # Akan mencetak 4


# Menambah dan Menghapus Elemen dalam List
# Anda dapat menambahkan elemen ke list dengan menggunakan metode append() atau insert(), dan menghapus elemen dengan menggunakan metode remove() atau pop(). Contoh:
my_list = [1, 2, 3, 4, 5]
my_list.append(6) # Menambahkan 6 ke list
print(my_list) # Akan mencetak [1, 2, 3, 4, 5, 6]
my_list.insert(2, 7) # Menyisipkan 7 pada indeks 2
print(my_list) # Akan mencetak [1, 2, 7, 3, 4, 5, 6]
my_list.remove(3) # Menghapus elemen 3
# Akan mencetak [1, 2, 7, 4, 5, 6]
print(my_list) 
popped_value = my_list.pop(4) # Menghapus elemen pada indeks 4 dan menyimpannya
print(my_list)
# Akan mencetak [1, 2, 7, 4, 6]
print(popped_value)
# Akan mencetak 5

# append insert remove

# nama.append("haryo")
# profile.insert(2, "Pria")
# profile.insert(60.7)

# print(profile)



# Operasi Pada List
# Anda dapat melakukan berbagai operasi pada list, seperti menggabungkan dua list, mengulang elemen, dan lainnya.
list1 = [1, 2, 3]
list2 = [4, 5, 6]
concatenated_list = list1 + list2
print(concatenated_list) # Akan mencetak [1, 2, 3, 4, 5, 6]
repeated_list = list1 * 3
print(repeated_list) # Akan mencetak [1, 2, 3, 1, 2, 3, 1, 2, 3]


# Match
# Anda menggunakan match untuk memeriksa ekspresi terhadap sejumlah kasus dan menjalankan blok kode yang sesuai dengan kasus pertama yang cocok. Format umumnya adalah sebagai berikut:
# Syntax:
# match term:
#     case pattern-1: action-1
#     case pattern-2: action-2
#     case pattern-3: action-3
#     case
# action-default


# Match case
#     lang = input("What's the programming language you want to learn?") match lang:
# case "JavaScript":
#     print("You can become a web developer.") case "Python":
#     print("You can become a Data Scientist") case "PHP":
#     print("You can become a backend developer")
# case "Solidity":
# print("You can become a Blockchain developer")
# case "Java":
# print("You can become a mobile app developer")
# case_:
# print("The language doesn't matter, what matters is solving problems.")


# Kombinasi dengan | (atau)
# Anda dapat menggunakan operator | untuk menggabungkan beberapa pattern dalam satu kasus. Contoh:
# match value:
    # case 1|2|3:
# Match 1, 2, or 3
    # case "apple" | "banana":
#Match "apple" or "banana"
    # case_:
# Default case