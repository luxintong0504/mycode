s1='''abcdefghijklmnopqrstuvwxyz 
ABCDEFGHIJKLMNOPQRSTUVWXYZ 
1234567890'''
for c in s1:
    print("%c -->%d 0x%x" %(c,ord(c),ord(c)))