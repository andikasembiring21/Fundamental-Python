angka=[23,5,3,13,2,3,22,53,25]

def genap(i):
    return i%2!=0

print(list(filter(genap,angka)))

#menggunakan clause
tp=[i for i in angka if genap(i)]
print(tp)

#menggunakan lambda
tp=list(filter(lambda x:x %2!=0,angka))
print(tp)
