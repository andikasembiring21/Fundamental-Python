"nilai_ulangan"
dp = 94+89+78+90
ds = 90+44+78+59

hasil_dp=dp/4
hasil_ds=ds/4

if(hasil_dp >75):
    print("lulus", hasil_dp)
else:
    print("gagal",hasil_dp)

if(hasil_ds >75):
    print("lulus", hasil_ds) 
else:
    print("gagal",hasil_ds)
    nilai_rajin=75/2
    nilai_aktif=70/2
    nilai_absen=77/2
    tp=(nilai_rajin+nilai_aktif+nilai_absen%5)/9
    print("nilai dongkrak ds ",tp+hasil_ds)

