angka = [[34, 6, 23, 43], [23, 46, 23, 23], [65, 34, 23, 64]]

for row in angka:
    for i in row:
        print(i,end=" ")
    print()

for i, row in enumerate(angka):
    for j,k in enumerate(row):
        print(f'[{i}][{j}]={k}',end=" ")
    print()
