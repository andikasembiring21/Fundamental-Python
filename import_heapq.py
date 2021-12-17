"""
masalah : bagaimana caranya kamu menentukan nilai terbesar dan terkecil di dalam sebuah collection
"""
#solusi
import heapq
num=[23,-23,32,2,-3]
print(heapq.nlargest(2,num))
print(heapq.nsmallest(2,num))

heapq.heapify(num)
print(num)

print(heapq.heappop(num))
print(heapq.heappop(num))
print(heapq.heappop(num))
print(heapq.heappop(num))
print(heapq.heappop(num))


tampung=[
    {'nama':'ddd','alamat':'adsf','price':'$34'},
    {'nama':'adf','alamat':'dfae','price':'$434'},
    {'nama':'tee','alamat':'dsafadf','price':'$334'},
    {'nama':'had','alamat':'eeww','price':'$534'},
    {'nama':'rer','alamat':'asdfasd','price':'$634'}
    ]
cheap=heapq.nsmallest(1,tampung,key=lambda s:s['price'])
expensive=heapq.nlargest(1,tampung,key=lambda s:s['price'])

print(cheap)
print(expensive)


def sorting(i):
    tp=[]
    for isi in i:
        heapq.heappush(tp,isi)
    return [heapq.heappop(tp) for j in range(len(tp))]

ini=sorting([6,34,3,4,23,64,3,75,7])
print(ini)


#untuk convert list di masukkan kedalam heap
sorting=[6,34,3,4,23,64,3,75,7]
heapq.heapify(sorting)
print(list(sorting))

