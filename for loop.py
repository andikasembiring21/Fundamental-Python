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
