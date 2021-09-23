from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017/')
db=client['pks']
print(db)

i={"nama" : "sapri",
   "umur" : 25,
   "alamat" : "jakarta"}

masuk=db.tours.insert(i)
print(masuk)


print("Daftar Mahasiswa Tahun 2019")
print("============================\n")
print("""Pilihan yang bisa diambil :
      1. Input Data
      2. Update Data
      3. Delete Data
      4. Show Data
      5. Exit
      """)

print("inpu pilihan anda: ")
inputan=input()

nomor=0
nama=""
nim=""
notelp=0
nik=""
alamat=""
asal_sekolah=""
jurusan=""
Pilihan_prodi=""

def data(n):
    for i in range (n):
        print("masukkan nama:")
        nama=input()
        print("masukkan nim: ")
        nim=input()
        print("masukkan nik: ")
        nik=input()
        print("masukkan no telephone: ")
        notelp=input()
        print("masukkan alamat: ")
        alamat=input()
        print("sekolah asal : ")
        asal_sekolah=input()
        print("jurusan saat di sekolah: ")
        jurusan=input()
        print("pilihan jurusan kuliah: ")
        pilihan_prodi=input()


