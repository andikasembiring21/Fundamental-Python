class kompleks:
    def __init__(i):
        i.nomor="kosong"
    def getnomor_rumah(i):  #digunakan untuk menampilkan hasil intruksi yang sudah diberikan
        return i.nomor
    def setnomor_rumah(i,nomor):   #digunakan untuk menangkap intruksi yang diberikan
        i.nomor=nomor
        
    n=property(getnomor_rumah,setnomor_rumah) #menggunakan property
    
siA=kompleks()
siB=kompleks()
siC=kompleks()
siA.setnomor_rumah("23 gang cendana")
siB.setnomor_rumah("32 gang rindu")
siC.n="114 gang hijau"              #menggunakan property

print(siA.nomor)
print(siB.nomor)
print(siC.n)
