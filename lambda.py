a=lambda b:b+1
print("sum ",a(23))

d={}
for i in range(5):
    d[i]=i**2
print(d)
    
print("===============================")

b={i:i**2 for i in range(5)}  #hasilnya sama dengan diatas namun caranya lebih singkat
print(b)

#penggunaan lambda dengan fungsi

tampung=lambda x,y:x**y+(x+y)

print(tampung(4,2))

print("=============================")

kalimat="tinakjf adsfjhadf adsf"
tampung=iter(kalimat)

while True:
    try:
        item=next(tampung)
        print(item)
    except StopIteration:
        break
