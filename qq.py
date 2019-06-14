import sys
import os
if len(sys.argv) < 2:
    print("error")

root=sys.argv[1]
for d,s,f in os.walk(root):
    print ("directory:%s" %d)
    print("sub-folder" + str(s))
    for fa in f:
        print(fa)