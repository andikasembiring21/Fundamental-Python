#melakukan perulangan dan memasukkan hasilnya ke dalam list
list=[]
for i in range(1,10,1):
    list.append(i)
print(list)

#menggunakan List Comprehension
list=[i for i in range(1,6)]
print(list)

#List Comprehension dengan kondisi di dalamnya
list=[i for i in range(1,10) if i % 2==0]
print(list)

#setiap i dipangkatkan dengan 3
list=[i ** 3 for i in range(1,6)]
print(list)

#mengubah warna menjadi huruf besar semua
warna=['red', 'orange', 'yellow', 'green', 'blue']
ubah=[i.upper() for i in warna]
print(ubah)

angka=[10, 3, 7, 1, 9, 4, 2, 8, 5, 6]
for i in (x ** 2 for x in angka if x%2!=0):
    print(i,end =" ")
