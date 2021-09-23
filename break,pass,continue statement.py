print("Selamat datang anak baru")
print("\n")

for kata in "Selamat datang anak baru":
    if(kata == "g"):
        break
    print("kata ",kata)
    
print("============================================")

for kata in "Selamat datang anak baru":
    if(kata == " "):
        break
    print("kata",kata)

print("============================================")

for kata in "Selamat datang anak baru":
    if(kata == "t"):
        continue
    print("kata ",kata)

print("============================================")

for kata in "Selamat datang anak baru":
    if(kata == "d"):
        pass
    print("kata ",kata)
