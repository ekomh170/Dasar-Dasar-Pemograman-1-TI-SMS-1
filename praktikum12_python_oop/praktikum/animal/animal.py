class animal :
    jumlah_kaki = ""
    memiliki_paruparu = ""
    jenis_kulit = ""
    jenis = ""
    BKSDA = 'Berikut ini adalah kategori hewan dilindungi :'

    def __init__(self, jumlah_kaki, memiliki_paruparu, jenis_kulit, jenis):
        self.jumlah_kaki = jumlah_kaki
        self.memiliki_paruparu = memiliki_paruparu
        self.jenis_kulit = jenis_kulit
        self.jenis = jenis
        
    def jenis(self, golongan):
        self.jenis += golongan
            
            
    def cetak(self):
        print(animal.BKSDA,
                '\nHewan Berkaki : ', format(self.jumlah_kaki, ','),
                '\nAlat Pernapasan : ', self.memiliki_paruparu,
                '\nBagaimana Jenis Kulitnya : ', self.jenis_kulit
                )

        
