#mencari nilai terbesar dengan fungsi

a=int(input("masukkan nilai 1: "))
b=int(input("masukkan nilai 2: "))
c=int(input("masukkan nilai 3: "))

def nilai_max(a,b,c):
    tampung=a
    if b>= tampung:
        tampung=b
    if c>= tampung:
        tampung=c
        
    return tampung

def nilai_min(a,b,c):
    tampung=a
    if b <= tampung:
        tampung=b
    if c <= tampung:
        tampung=c
    return tampung

print("\n==============================")
print("hasil nilai max ",nilai_max(a,b,c))
print("hasil nilai min ",nilai_min(a,b,c))

