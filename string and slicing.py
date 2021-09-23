kata="siapa kita" #huruf pertama memiliki index 0 jadi s=0,i=1,a=2,p=3,a=4 dan seterusnya
print(kata[2:4])  #angka 2 index start sedangkan 4 merupakan jumlah huruf yang akan di ambil dengan 2-4 = 2

print(kata[-5:-2])
print(kata[-2])
print(kata[-4])

potong1= slice(8)
potong2= slice(2,3,3)

print(kata[potong1]) #akan berhenti di index ke 7 dengan output "siapa ki"
print(kata[potong2]) #output "a"


print("kata[6] = %s"%kata[6])   #perhitungan index dari depan
print("kata[-6] = %s"%kata[-6]) #perhitungan index dari belakang
print("kata[2:4] =%s"%kata[2:4])


"""challenge:
input  : "mari belajar bersama"
output :
          -be
          -sama
          -ar
"""
