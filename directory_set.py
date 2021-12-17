anggota = {"dini":12,"santi":53,"budi":21,"wiwik":53,"susanti":12,"pandri":42}

print(anggota)
#len digunakan untuk menghitung panjang isi anggota
print(len(anggota))

#mengecek isi dari anggota
if anggota:
    print("variabel anggota berisi")
else:
    print("variabel anggota kosong")

anggota.clear()

if anggota:
    print("variabel anggota berisi")
else:
    print("variabel anggota kosong")

#menampilakn value and key 
anggota = {"dini":12,"santi":53,"budi":21,"wiwik":53,"susanti":12,"pandri":42}

print(list(anggota.keys()))
print(list(anggota.values()))
print(list(anggota.items()))
