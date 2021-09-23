import pymongo
import pprint
from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017/')
db=client['pks']

i={"nama" : "susi",
   "umur" : 23,
   "alamat" : "ja"}

#insert ke dalam database
masuk=db.tours.insert_one(i)

#menampilkan seluruh isi database
for i in db.tours.find():
    pprint.pprint(i)

print("==========================================")

#menampilakn nama tertentu dengan ketentuan nama
cari=db.tours.find_one({"nama":"susi"})
print(cari)

#menghapus salah satu isi data
delete=db.tours.delete_one({"nama":"susi"}) #kalau delet_many menghapus keseluruhan data
print(delete)
