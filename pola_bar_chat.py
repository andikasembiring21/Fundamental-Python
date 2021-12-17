angka=[23,5,3,13,2,3]
print("membuat bar chat dari angka: ")
print(f'index{"nilai" :>8} Bar ')

for i, n in enumerate(angka):
    print(f'{i:>5}{n:>8} {"*" * n}')
