class parent:  #class parent
    name=""
    age=0
    alamat=""
    def tampil(i):
        print("name: ",i.name,"\nage: ",i.age)

#inheritance class
class child(parent): #parameter di dalam class child harus berupa parrent class
    def tpl(z):
        print("alamat: ",z.alamat)

#inisialisasi object child
tp=child()
tp.name="blablabla"
tp.age=23
tp.alamat="jln.madura"

tp.tampil()
tp.tpl()

class ayah:
    def __init__(i,nama="ada",umur=43,jumlah_anak=4,pekerjaan="d"):
        i.nama=nama
        i.umur=umur
        i.jumlah_anak=jumlah_anak
        i.pekerjaan=pekerjaan

    def hobi(i):
        print("ayah hobi memancing di di umur",i.umur)

class bungsu(ayah):
    pass

tp=ayah("blablbla",25,5,"karyawan")
print(tp.nama)
print(tp.umur)
print(tp.jumlah_anak)
print(tp.pekerjaan)

tp.hobi()

class stor:
    def __init__(i,nama,cabang,hasil):
        i.nama=nama
        i.cabang=cabang
        i.hasil=hasil
    def tp_nama(i):
        print(i.nama)
        
    def tp_cabang(i):
        print(i.cabang)
        
    def tp_hasil(i):
        print(i.hasil)
        
    def mainan(i):
        print("banyak mainan")
        
class sub_stor(stor):
    def perabot(i):
        print("cuma perabot")

class last_store(sub_stor):
    def food(i):
        print("makanan oiy")

class pemilik:
    def __init__(i,nama,alamat,pengalaman):
        i.nama=nama
        i.alamat=alamat
        i.pengalaman=pengalaman
    def snama(i):
        return i.nama
    def salamat(i):
        return i.alamat
    def spengalaman(i):
        return i.pengalaman

class tampil(stor,pemilik):
    def __init__(i,nama,alamat,pengalaman,cabang,hasil):
        stor.__init__(nama,cabang,hasil)
        pemilik.__init__(i,alamat,pengalaman)


tp=last_store("david",56,"bobi")
tp.mainan()
tp.perabot()
tp.food()


