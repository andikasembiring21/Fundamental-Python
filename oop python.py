class barang:
    baju="HugoSport"
    celana='jeans'
    size_celana=39

tampung=barang()
print("celana: ",tampung.celana,"\nukuran: ",tampung.size_celana)

print("====================")

class motor:
    def __init__(merek,kecepatan,warna,tahun_edaran):  # __init__() fungsi ini digunakan untuk memanggil secara otomatis setiap kali kelas digunakan untuk membuat objek baru
       merek.kecepatan=kecepatan
       merek.warna=warna
       merek.tahun_edaran=tahun_edaran

mt1=motor(150,"hitam",2015)
mt2=motor(210,"merah",2019)

print("====================")
print(mt1.kecepatan)
print(mt1.warna)
print(mt1.tahun_edaran)
print("====================")
print(mt2.kecepatan)
print(mt2.warna)
print(mt2.tahun_edaran)
print("====================")

class person:
    def __init__(i,name,age,tinggi,alamat):
        i.name=name
        i.age=age
        i.tinggi=tinggi
        i.alamat=alamat

    def child(test):
        print(" perkenal kan nama saya "+test.name)

p=person("blabla",21,180,"jln,cempaka")

print(p.name)
print(p.age)
print(p.tinggi)
print(p.alamat)

p.child()

print("====================")

class sepeda:
    pass
sp=sepeda()
sp.jenis="downhill"
sp.berat=50

print(sp.jenis,"\n",sp.berat,"kg")

