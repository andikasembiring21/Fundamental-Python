restoranA={
    '1 - Ikan kakakp':20000,
    '2 - ayam panggang':8000,
    '3 - gulai baung':12000
    }

restoranB={
    '1 - gulai baung':12000,
    '2 - sambal cumi-cumi':21000,
    '3 - bakso':20000
    }

def dedupe(items):
    seen=set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)

a=[1,2,4,5,6,4,3,4,6]
p=list(dedupe(a))
print(p)
