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
    nilai_rajin=70/2
    nilai_aktif=65/2
    nilai_absen=77/2
    tp=(nilai_rajin+nilai_aktif+nilai_absen%4)/10
    akhir=tp+hasil_ds
    if(akhir>75):
        print("hasil dongkrak : ",akhir)
    else:
        print("gagal",akhir)
    

