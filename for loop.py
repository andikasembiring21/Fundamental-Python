from functools import reduce

data=[1,2,3,4,5]

data1=filter(lambda x : x% 2 ==0,data)
print(reduce(max,data1))

data=("satu","dua","tiga","empat","lima","enam","tujuh","delapan")
dataAngka=(1,2,3,4,5,6)
dataCampur=(1,"budi", 1996,("bekasi","jawa barat"),["sd","smp","sma"])

print("elemen terakhir : ",data[:-1])

daftar=[9,1,3,12,3,1,3,5,6,7,34,7,8]

 

daftar=daftar[:-4]

 

print(max(sorted(daftar)))

mhs2=("wati","cirebon","jawa barat","membaca",12,"Juni",1999)
mhs1=("budi","majalengka","jawa barat","memancing",17,"April",1996)
daftar=[mhs1,mhs2]

 

i=0
for z in daftar:
    for x in daftar[i]:
        if daftar[i].index(x)==0:
            print(x)
    i=i+1


color="blue","red","pink","gray","silver"

for i in color:
    print(i)

tp=0
for i in range(1,10+1):
    tp+=i
    print(tp)
    

for i in range(1,100+1):
    if(i % 2 == 1):
        print("ganjil ",[i])
    else:
        print("genap ",[":)"])

total=0
num=5

while(num <=10):
    total=total+num
    num+=1
    print("total ",total)


#nested loop

for angka in range(4):
    for angka1 in range(1,5):
        print(angka,",",angka1)
