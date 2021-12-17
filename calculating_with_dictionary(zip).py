barang={
    'meja':17.000,
    'kursi':43.000,
    'kayu':34.000,
    'rak kayu':34.000,
    'buku':32.000,
    'spidol':23.000
    }

#akan menampilkan harga terkecil berdasarkan nilai harga terendah
harga_terkecil=min(zip(barang.values(),barang.keys()))
print(harga_terkecil)

#akan mengeluarkan tampilan key yang paling kecil berdasarkan urutan kode ASCI
harga_terkecil=min(zip(barang.keys(),barang.values()))
print(harga_terkecil)

#menggunakan fungsi min dan max untuk mencari nilai terbesar dan terkecil
mini=min(barang,key=lambda k:barang[k])
ma=max(barang,key=lambda k:barang[k])
print(mini)
print(ma)

#akan mengurutkan dari barang terendah ke barng tertinggi 
tp=sorted(zip(barang.values(),barang.keys()))
print(tp)

#berikut cara menggabungkan beberapa list menjadi satu
angka=[1,2,3,4,5,6,7,8,9,10]
abjad=['a','b','c','d','e','f','g','h','i','j']

union=zip(angka,abjad)
tampung=list(union)

print(tampung)

#nah kita sudah bisa mengakses indek list tersebut dan di dalam list tersebut sudah menjadi value dan key 
print(tampung[2])


#perulangan menggunakan zip

for i,tp in zip(angka,abjad):
    print(i,tp)


#mengembalikan keadaan semula setelah di zip
gabung=tampung  #nilai tampung yang sudah di listkan di masukkan ke dalam variabel tampung yaitu gabung

asal_angka,asal_abjad=zip(*gabung) #disini terjadi proses unzip mengembalikan nilai seperti semula

print(asal_angka)
print(asal_abjad)

