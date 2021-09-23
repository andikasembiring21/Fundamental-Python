angka=14
i=0
var1=0
var2=1
while(i<angka):
    if(i<=1):
        next=i
    else:
        next=var1+var2
        var1=var2
        var2=next

    print(next)
    i=i+1
