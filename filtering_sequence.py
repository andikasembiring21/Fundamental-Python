import math
pelajaran=['matematika','ips','ipa','biologi','fisika','agama','bahasa indonesia','bahasa inggris','bahasa mandarin','bahasa arab']
nilai_akhir=[70,75,60,40,50,20,90,93,45,77]

j=[n for n in nilai_akhir if n>75]
print(j)

j=[n for n in nilai_akhir if n<75]
print(j)


nilai=[3,5,2,4,5,3,4]

def n(nilai):
    try:
        x=int(nilai)
        return True
    except valueError:
        return False

inilai=list(filter(n,nilai))
print(inilai)

tp=[math.sqrt(p) for p in nilai if p>0]
print(tp)

tp=[p if p>3 else 0 for p in nilai]
print(tp)
