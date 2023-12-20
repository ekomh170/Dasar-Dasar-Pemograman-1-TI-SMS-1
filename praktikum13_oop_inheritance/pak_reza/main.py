class Orang:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def makan(self):
        print("Saya bisa makan")

    def cetak(self):
        print("Nama saya", self.fname, self.lname)


class Mahasiswa(Orang):
    def __init__(self, fname, lname, prodi, angkatan):
        super().__init__(fname, lname)
        self.prodi = prodi
        self.angkatan = angkatan

    def display(self):
        super().cetak()
        print("Saya prodi", self.prodi, self.angkatan)


class Pegawai(Orang):
    def bekerja(self):
        print("Saya bekerja")

# Objek Orang
x = Orang("Anto", "Hud")
x.cetak()

# Objek Mahasiswa
y = Mahasiswa("Dwi", "Astuti", "Teknik Informatika", 2023)
y.display()
y.makan()

# Objek Pegawai
agus = Pegawai("Agus", "Rahman")
