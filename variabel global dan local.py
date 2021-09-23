i="yes"                  #global
def lingkup_variabel():
    global i             #inisialisai variabel global di dalam fungsi
    i="Run"              #variabel local
    print(i)
    
lingkup_variabel()

print(i)

"""inisialisasi variabel dengan cara global dapat di gunakan di luar fungsi
sedangkan inisialisasi variabel local hanya dapat digunakan di dalam ruang lingkup fungsi saja
untuk mengakses dan mengeluarkan nilai yang ada di dalam fungsi gunakan keyword "global"
"""
#contoh:

panjang=4
def luas_lingkaran():
    global panjang
    lebar=5
    print("luas lingkaran : ",panjang*lebar)

luas_lingkaran()




