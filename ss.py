JINGDU = 0.00000000001
x = 1
y = int(input('please input a number: '))
a = 1
while a > JINGDU:
    x = (y/x + x)/2
    a = abs(y - x*x)
print(x)
