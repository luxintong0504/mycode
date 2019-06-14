a=[5,4,8,7,6]
i=len(a)
while i != 1 :
    for j in range(0,i-1):
        if a[j] > a[j+1]:
            a[j],a[j+1] = a[j+1],a[j]
    i = i-1
print(a)        