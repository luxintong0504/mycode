def bis(l,x):
    low=0
    high=len(l)-1
    while low<=high:
        i=(low+high)//2
        if l[i]>x:
            high=i-1
        elif l[i]<x:
            low=i+1
        elif l[i]==x:
            return i
        print(low)
        print(high)            
    return "oops"
a=[1,2,3,4,5]
print(bis(a,7))