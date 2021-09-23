import math
print("tangen : ",math.tan(120))
print("cosinus ",math.cos(60))


def tambah(var1,var2=5): #var2 diberikan nilai default, saat programer memasukkan 1 inputan maka program akan tetap di jalan kan karna terdapat nilai default
    return var1+var2     # def tambah (var1=12,var2=4)
                         #      return 12+4 
a1=tambah(12,4)          # print(a1) 16
a2=tambah(9)
a3=tambah(-3,4)

print(a1)
print(a2)
print(a3)

