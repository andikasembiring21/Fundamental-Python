import random

print("randome input number: ")
n=random.randint(1,100)  #acak angka dengan ketentuan (start,stop)
list1=list()
for i in range(1,int(n)+1):
    list1.append(i)
print(list1)

print("start index: ")
s=input()
print("end index: ")
e=input()

tampung=list1[int(s):int(e)]
print(tampung)

list1.remove(4)
print("remove index ke-4 : ",list1)

randome=random.randrange(1,int(n)+1,10) #mengacak angka dengan ketentuan (start,stop,step)

#percabangan di dalam list

if randome in tampung:
    print("anggota",randome)
else:
    print("bukan anggota",randome)

